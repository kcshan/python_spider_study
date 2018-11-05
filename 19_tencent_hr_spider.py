# encoding: utf-8

import requests
from lxml import etree
import math


# 1.将目标网站上的页面抓取下来
BASE_DOMAIN = "https://hr.tencent.com/"
HEADERS = {
    "Referer": "https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}


# 获取一共多少页
def get_pages(url):
    resp = requests.get(url=url, headers=HEADERS)
    text = resp.text
    html = etree.HTML(text)
    pages = math.ceil(float(html.xpath("//span[@class='lightblue total']/text()")[0])/10)
    return pages


def get_position_abouts(url):
    resp = requests.get(url=url, headers=HEADERS)
    text = resp.text
    html = etree.HTML(text)
    trEles = html.xpath("(//tr[@class='even'] | //tr[@class='odd'])")
    position_abouts = list()
    for trEle in trEles:
        # 职位名称 .//td/a[@href]/text()
        position_name = trEle.xpath(".//td/a[@href]/text()")[0]
        # 职位详情页面地址 .//td/a/@href
        detail_url = trEle.xpath(".//td/a/@href")[0]
        detail_url = BASE_DOMAIN + detail_url
        # 职位类别 .//td[2]/text()
        position_type = trEle.xpath(".//td[2]/text()")[0]
        # 职位招聘数量 .//td[3]/text()
        position_num = trEle.xpath(".//td[3]/text()")[0]
        # 职位地点 .//td[4]/text()
        position_city = trEle.xpath(".//td[4]/text()")[0]
        # 职位发布时间 .//td[5]/text()
        position_time = trEle.xpath(".//td[5]/text()")[0]
        #print(etree.tostring(trEle, encoding="utf-8").decode("utf-8"))
        position_about = {
            "position_name": position_name,
            "detail_url": detail_url,
            "position_type": position_type,
            "position_num": position_num,
            "position_city": position_city,
            "position_time": position_time,
        }
        position_abouts.append(position_about)
    return position_abouts


def parse_detail_url(url):
    resp = requests.get(url=url, headers=HEADERS)
    text = resp.text
    html = etree.HTML(text)
    # 工作职责
    ulDutyEle = html.xpath("//ul[@class='squareli']")[0]
    operating_dutys = ulDutyEle.xpath(".//li/text()")
    operating_duty = ','.join(operating_dutys)
    # 工作要求
    ulJobEle = html.xpath("//ul[@class='squareli']")[1]
    job_requirements = ulJobEle.xpath(".//li/text()")
    job_requirement = ','.join(job_requirements)
    return {
        "operating_duty": operating_duty,
        "job_requirement": job_requirement
    }


if __name__ == "__main__":
    # 第一页
    first_url = BASE_DOMAIN + "position.php?lid=&tid=&keywords=python&&start=0"
    pages = get_pages(first_url)
    detail_infos = list()
    for page in range(0, 1):
        detail_url = BASE_DOMAIN + "position.php?lid=&tid=&keywords=python&&start=%d" % (page * 10)
        # 拿到每个职位对应的详情页
        position_abouts = get_position_abouts(detail_url)
        for position_about in position_abouts:
            # 从详情页中取出工作职责和工作要求
            works = parse_detail_url(position_about['detail_url'])
            position_about["operating_duty"] = works["operating_duty"]
            position_about["job_requirement"] = works["job_requirement"]
            print(position_about)
        # print(position_abouts)

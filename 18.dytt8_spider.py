# encoding: utf-8

import requests
from lxml import etree


# 1.将目标网站上的页面抓取下来
BASE_DOMAIN = "https://www.dy2018.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Referer": "https://www.dy2018.com/html/gndy/dyzz/"
}
URL = "https://www.dy2018.com/html/gndy/dyzz/index.html"


def get_detail_urls(url):
    resp = requests.get(url=url, headers=HEADERS)
    # print(resp.encoding) # ISO-8859-1
    # text = resp.content.decode("gbk")
    text = resp.text
    html = etree.HTML(text)
    # tables = html.xpath("//table[@class='tbspan']")
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # for table in tables:
    #     print("========")
    #     print(etree.tostring(table, encoding="utf-8").decode("utf-8"))
    # ===============================
    # for detail_url in detail_urls:
    #     detail_url = BASE_DOMAIN + detail_url
    #     print(detail_url)
    # ===============================
    # def abc(url):
    #    return  BASE_DOMAIN + url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = abc(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1
    # ===============================
    # 下面这句等价于上面
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    # print(detail_urls)
    return detail_urls

def parse_info(info, rule):
    return info.replace(rule, "").strip()


def parse_detail_page(url):
    resp = requests.get(url=url, headers=HEADERS)
    text = resp.content.decode("gbk")
    html = etree.HTML(text)
    # //div[@class="title_all"]/h1/text()
    title = html.xpath("//div[@class='title_all']/h1/text()")[0]
    # //div[@id='Zoom']//img/@src
    zoomEle = html.xpath("//div[@id='Zoom']")[0]
    # //img/@src
    imgs = zoomEle.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    # //p[position()>1]
    infos = zoomEle.xpath(".//p[position()>1]/text()")
    year = ""
    country = ""
    category = ""
    douban_rating = ""
    duration = ""
    director = ""
    actors = list()
    profile = ""
    list_name = ["◎年　　代", "◎产　　地", "◎类　　别", "◎豆瓣评分", "◎片　　长", "◎导　　演", "◎主　　演", "◎简　　介"]
    for index, info in enumerate(infos):
        if info.startswith(list_name[0]):
            year = parse_info(info, list_name[0])
        elif info.startswith(list_name[1]):
            country = parse_info(info, list_name[1])
        elif info.startswith(list_name[2]):
            category = parse_info(info, list_name[2])
        elif info.startswith(list_name[3]):
            douban_rating = parse_info(info, list_name[3])
        elif info.startswith(list_name[4]):
            duration = parse_info(info, list_name[4])
        elif info.startswith(list_name[5]):
            director = parse_info(info, list_name[5])
        elif info.startswith(list_name[6]):
            actor = parse_info(info, list_name[6])
            actors.append(actor)
            for x in range(index + 1, len(infos)):
                if infos[x].startswith(list_name[7]):
                    profile = parse_info(infos[x + 1], list_name[7])
                    break
                actor = infos[x].strip()
                actors.append(actor)
    # //td[@bgcolor="#fdfddf"]//a
    download_url = html.xpath("//td[@bgcolor='#fdfddf']//a/text()")[0]
    # print(download_url)
    movie = {
        "title": title,
        "cover": cover,
        "year": year,
        "country": country,
        "category": category,
        "douban_rating": douban_rating,
        "duration": duration,
        "director": director,
        "actors": actors,
        "profile": profile,
        "screenshot": screenshot,
        "download_url": download_url
    }
    return movie

def spider():
    base_url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
    base_url_other = "https://www.dy2018.com/html/gndy/dyzz/index_{}.html"
    movies = list()
    for x in range(1, 8):
        if x == 1:
            url = base_url
        else:
            url = base_url_other.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            # print(detail_url)
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)
        break

# 2.将抓取下来的数据根据一定的规则进行提取
movies = list()
if __name__ == "__main__":
    spider()



# encoding: utf-8

import requests
from lxml import etree


# 1.将目标网站上的页面抓取下来
url = "https://coding.imooc.com/class/100.html"
BASE_DOMAIN = "https://coding.imooc.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def get_class_title(num, url):
    try:
        resp = requests.get(url=url, headers=HEADERS)
        # print(resp.encoding) # ISO-8859-1
        # text = resp.content.decode("gbk")
        text = resp.content.decode("utf-8")
        # with open("imooc.html", "w") as f:
        #     f.write(text)

        html = etree.HTML(text)
        title = html.xpath("//div[@class='title-box ']/h1/text()")[0]
        class_title = "%d-%s" % (num, title)
        # print("%d-%s" % (num, title))
    except:
        print("%d-%s" % (num, "此页面无课程"))

def spider():
    base_url = "https://coding.imooc.com/class/{}.html"
    titles = list()
    for x in range(100, 300):
        url = base_url.format(x)
        title = get_class_title(x, url)
        titles.append(title)
    print(len(titles))
    for title in titles:
        print(title)


# 2.将抓取下来的数据根据一定的规则进行提取
movies = list()
if __name__ == "__main__":
    spider()



# encoding: utf-8

import requests
from lxml import etree


# 1.将目标网站上的页面抓取下来
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}
url = "https://movie.douban.com/cinema/nowplaying/hangzhou/"
resp = requests.get(url=url, headers=headers)
text = resp.text
# print(text)
# with open("douban_movie.html", "w", encoding="utf-8") as f:
#     f.write(resp.content.decode("utf-8"))
# resp.text 返回的是经过解码的字符串 是str(unicode)类型
# resp.content 返回的是一个原生的字符串，就是从网页上抓取下来的，没有经过处理的字符串，bytes类型

# 2.将抓取下来的数据根据一定的规则进行提取
movies = list()
html = etree.HTML(text)
# //ul[@class="lists"]
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul, encoding="utf-8").decode("utf-8"))
# ./li
lis = ul.xpath("./li")
for li in lis:
    # print(etree.tostring(li, encoding="utf-8").decode("utf-8"))
    # @data-title
    title = li.xpath("@data-title")[0]
    # @data-score
    score = li.xpath("@data-score")[0]
    # @data-duration
    duration = li.xpath("@data-duration")[0]
    # @data-region
    region = li.xpath("@data-region")[0]
    # @data-director
    director = li.xpath("@data-director")[0]
    # @data-actors
    actors = li.xpath("@data-actors")[0]
    # .//img/@src
    thumbnail = li.xpath(".//img/@src")[0]
    # print(thumbnail)
    movie = {
        "title": title,
        "score": score,
        "duration": duration,
        "region": region,
        "director": director,
        "actors": actors,
        "thumbnail": thumbnail
    }
    movies.append(movie)

print(movies)


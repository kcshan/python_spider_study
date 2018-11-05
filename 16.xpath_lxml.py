from lxml import etree


parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("tencent.html", parser=parser)
# 1.获取所有tr标签
# //tr
trs = html.xpath("//tr")
for tr in trs:
    pass
    # print(tr)
    # print(etree.tostring(tr, encoding="utf-8").decode("utf-8"))

# 2.获取第2个tr标签
# //tr[2]
trs = html.xpath("//tr[2]")
# for tr in trs:
#     # pass
#     print(tr)
#     print(etree.tostring(tr, encoding="utf-8").decode("utf-8"))
# print(etree.tostring(trs[0], encoding="utf-8").decode("utf-8"))

# 3.获取所有class等于even的tr标签
# //tr[@class="even"]
trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     # pass
#     print(tr)
#     print(etree.tostring(tr, encoding="utf-8").decode("utf-8"))


# 4.获取所有a标签的href属性
# //a/@href
alist = html.xpath("//a/@href")
# print(len(alist))
# for a in alist:
#     # pass
#     print(a)

# 5.获取所有职位信息（纯文本）
# //tr[position()>1]
# .//a/@href
# ./td/text()
positions = list()
trs = html.xpath("//tr[position()>1]")
for tr in trs:
    # pass
    try:
        href = tr.xpath(".//a/@href")[0]
        fullurl = "https://hr.tencent.com/" + href
        # print(fullurl)
        title = tr.xpath("./td[1]//text()")[0]
        # print(title)
        category = tr.xpath("./td[2]//text()")[0]
        # print(category)
        nums = tr.xpath("./td[3]//text()")[0]
        # print(nums)
        address = tr.xpath("./td[4]//text()")[0]
        # print(address)
        pubtime = tr.xpath("./td[5]//text()")[0]
        # print(pubtime)
        position = {
            "url": fullurl,
            "title": title,
            "category": category,
            "nums": nums,
            "address": address,
            "pubtime": pubtime
        }
        positions.append(position)
    except Exception as ret:
        print(ret)

#     print(etree.tostring(tr, encoding="utf-8").decode("utf-8"))
print(positions)

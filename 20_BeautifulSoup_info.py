from bs4 import BeautifulSoup


position_str = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tr class="h">
        <td class="l" width="374">职位名称</td>
        <td>职位类别</td>
        <td>人数</td>
        <td>地点</td>
        <td>发布时间</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45294&keywords=&tid=87&lid=0">22989-AI产品前端软件开发工程师（深圳/北京/杭州）</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45287&keywords=&tid=87&lid=0">25663-腾讯云交通行业总监（深圳）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45289&keywords=&tid=87&lid=0">22989-AI产品高级后台软件开发工程师(深圳/北京/杭州）</a>
        </td>
        <td>技术类</td>
        <td>3</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45283&keywords=&tid=87&lid=0">28603-122
            支付安全大数据工程师（深圳）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45285&keywords=&tid=87&lid=0">25663-腾讯云广电行业总监（北京/深圳）</a><span
                class="hot">&nbsp;</span></td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45286&keywords=&tid=87&lid=0">25663-腾讯云工业行业总监（深圳）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45274&keywords=&tid=87&lid=0">WXG10-113
            企业微信高级后台开发工程师（广州）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>广州</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45277&keywords=&tid=87&lid=0">WXG02-121
            微信数据挖掘工程师（深圳）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45278&keywords=&tid=87&lid=0">21557-音视频网络技术高级开发工程师（深圳）</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>深圳</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=45279&keywords=&tid=87&lid=0">21557-Software
            Engineer – VR (Silicon Valley/Shenzhen/Beijing)</a></td>
        <td>技术类</td>
        <td>2</td>
        <td>美国</td>
        <td>2018-11-01</td>
    </tr>
    <tr class="f">
        <td colspan="5">
            <div class="left">共<span class="lightblue total">1362</span>个职位</div>
            <div class="right">
                <div class="pagenav"><a href="javascript:;" class="even" id="test">上一页</a><a class="active"
                                                                                                 href="javascript:;">1</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=10#a">2</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=20#a">3</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=30#a">4</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=40#a">5</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=50#a">6</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=60#a">7</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=70#a">...</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=1360#a">137</a><a
                        href="position.php?keywords=请输入关键词&lid=0&tid=87&start=10#a" id="next">下一页</a>
                    <div class="clr"></div>
                </div>
            </div>
            <div class="clr"></div>
        </td>
    </tr>
</table>

"""

# 使用lxml解释器
bs = BeautifulSoup(position_str, "lxml")
# print(bs.prettify())


# 1.获取所有tr标签
# bs.find_all("tr")
# trs = bs.find_all("tr")
# for tr in trs:
#     print(tr)

# 2.获取第2个tr标签
# bs.find_all("tr", limit=2)[1]
# tr = bs.find_all("tr", limit=2)[1]
# print(tr)

# 3.获取所有class等于even的tr标签
# trs = bs.find_all("tr", class_="even")
# for tr in trs:
#     print(tr)
# =======================================
# trs = bs.find_all("tr", attrs={"class": "even"})
# for tr in trs:
#     print(tr)

# 5.获取所有id等于test, class等于even的a标签
# a_s = bs.find_all("a", id="test", class_="even")
# for a in a_s:
#     print(a)
# =======================================
# a_s = bs.find_all("a", attrs={"class": "even", "id": "test"})
# for a in a_s:
#     print(a)

# 5.获取所有a标签的href属性
# a_s = bs.find_all("a")
# for a in a_s:
#     print(a["href"])
#     # =======================================
#     print(a.attrs["href"])

# 6.获取所有职位信息（纯文本）
trs = bs.find_all("tr")[1:]
trs.pop()
for tr in trs:
    # tds = tr.find_all("td")
    # title = tds[0].string
    # category = tds[1].string
    # nums = tds[2].string
    # city = tds[3].string
    # time = tds[4].string
    # position = {
    #     "title": title,
    #     "category": category,
    #     "nums": nums,
    #     "city": city,
    #     "time": time,
    # }
    # infos = list(tr.strings)
    infos = list(tr.stripped_strings)
    title = infos[0]
    category = infos[1]
    nums = infos[2]
    city = infos[3]
    time = infos[4]
    position = {
        "title": title,
        "category": category,
        "nums": nums,
        "city": city,
        "time": time,
    }
    print(position)
import requests


url = "http://www.baidu.com/s"
kw = {
    "wd": "中国"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
resp = requests.get(url=url, params=kw, headers=headers)
# 查看返回的字符串
# print(type(resp.text))  # <class 'str'>
# print(resp.text)

# 查看返回的字节流
# print(type(resp.content))  # <class 'bytes'>
# print(resp.content)
# print(resp.content.decode("utf-8"))
with open("baidu.html", "w", encoding="utf-8") as fp:
    fp.write(resp.content.decode("utf-8"))

# 查看完整的url地址
print(resp.url)

# 查看响应头部字符编码
print(resp.encoding)

# 查看响应码
print(resp.status_code)

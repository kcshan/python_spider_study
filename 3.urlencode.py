from urllib import request
from urllib import parse
# data = {"name": "爬虫基础", "greet": "hello world", "age": 100}
# qs = parse.urlencode(data)
# print(qs) # name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=hello+world&age=100

url = "http://www.baidu.com/s"
param = {"wd": "刘德华"}
r_url = url + "?" + parse.urlencode(param)
req = request.urlopen(r_url)
print(req.read())

# params = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=hello+world&age=100"
# print(parse.parse_qs(params))
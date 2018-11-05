from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

req = request.urlopen(url)
print(req.read())

req = request.Request(url, headers=header)
res = request.urlopen(req)
print(res.read())


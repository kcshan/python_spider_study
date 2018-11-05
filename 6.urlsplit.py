#encoding:utf-8

from urllib import parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.baidu.com/s?wd=python&username=thomas#1"
result2 = parse.urlsplit(url)
print(result2)
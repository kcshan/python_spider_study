#encoding:utf-8

from urllib import parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.baidu.com/s?wd=python&username=thomas#1"

result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)

print(result1)
print(result2)
print('-----------------------')
print("scheme:", result1.scheme)
print("netloc:", result1.netloc)
print("path:", result1.path)
print("params:", result1.params)
print("query:", result1.query)
print("fragment:", result1.fragment)
# print(result2)
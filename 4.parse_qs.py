#encoding:utf-8

from urllib import parse

params = {"name": "张三", "age": 12}
qs = parse.urlencode(params)
parse_qs = parse.parse_qs(qs)
print(parse_qs) # {'name': ['张三'], 'age': ['12']}
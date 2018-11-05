#encoding:utf-8

from urllib import request

request.urlretrieve("http://www.baidu.com/", "baidu.html")
# print(resp)
# https就失败↓
request.urlretrieve('http://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1533620338486&di=73cd8a5aa13c8ed4b4461137fed3bf75&imgtype=0&src=http%3A%2F%2Fwww.07073.com%2Fuploads%2F170322%2F17598508_142130_1_lit.jpg','luban.jpg')

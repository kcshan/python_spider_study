#encoding:utf-8

import ssl
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context

dapeng_url = 'http://www.renren.com/880151247/profile'
headers = {
    'User-Agent':'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}
req = request.Request(url=dapeng_url, headers=headers)
resp = request.urlopen(req)

with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))
    fp.close()
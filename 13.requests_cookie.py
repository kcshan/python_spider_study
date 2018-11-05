import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

dapeng_url = 'http://www.renren.com/880151247/profile'
login_url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent':'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
data = {
    'email': '18210677984',
    'password': 'baiqi521@'
}
# resp = requests.post(url=login_url, headers=headers, params=data)
# print(resp.cookies)
# print(resp.cookies.get_dict())
session = requests.Session()
session.post(url=login_url, params=data, headers=headers)
resp = session.get(url=dapeng_url)
print(resp.text)

with open("renren.html", "w", encoding="utf-8") as fp:
    '''
        write函数必须写入一个str数据类型
        resp.read()读出来是一个bytes数据类型
        bytes --> decode --> str
        str   --> encode -->bytes
        print()函数之后无法写入html
    '''
    fp.write(resp.content.decode("utf-8"))
    fp.close()


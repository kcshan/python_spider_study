import ssl
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context

# 大鹏董成鹏主页: http://www.renren.com/880151247/profile
# 人人登录url: http://www.renren.com/PLogin.do

dapeng_url = 'http://www.renren.com/880151247/profile'
headers = {
    'User-Agent':'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Cookie': 'ick_login=ac8e89c4-ae91-4225-b8d1-7b39aaffca40; anonymid=jnj4dykc22iz6z; depovince=GW; _r01_=1; JSESSIONID=abcx5yZCclgxzdf78KxAw; jebecookies=612ecf07-be85-45bc-a65e-a7d0462fa5cf|||||; jebe_key=0440cbf7-23f5-4bd7-8345-99447212bd51%2Ccfcd208495d565ef66e7dff9f98764da%2C1535353936085%2C0%2C1535360378972%7C%7C%7C%7C1540265992456; _de=6F40E08FE9F6D58B6B70847FA302AABB; p=8962045d00326cd5644228c333ec78d40; ap=967768340; first_login_flag=1; ln_uact=18210677984; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=ecfdd184a603ede4c208e04a25d119b10; societyguester=ecfdd184a603ede4c208e04a25d119b10; id=967768340; xnsid=60f628dd; loginfrom=syshome'
}
req = request.Request(url=dapeng_url, headers=headers)
resp = request.urlopen(req)

with open("renren.html", "w", encoding="utf-8") as fp:
    '''
        write函数必须写入一个str数据类型
        resp.read()读出来是一个bytes数据类型
        bytes --> decode --> str
        str   --> encode -->bytes
        print()函数之后无法写入html
    '''
    fp.write(resp.read().decode("utf-8"))
    fp.close()
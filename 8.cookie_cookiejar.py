import ssl
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

ssl._create_default_https_context = ssl._create_unverified_context

# 大鹏董成鹏主页: http://www.renren.com/880151247/profile
# 人人登录url: http://www.renren.com/PLogin.do
dapeng_url = 'http://www.renren.com/880151247/profile'
login_url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent':'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

def get_opener():
    # 1. 登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    # 1.4 使用opener发送登录的请求(人人网的邮箱和密码)
    data = {
        'email': '18210677984',
        'password': 'baiqi521@'
    }

    req = request.Request(url=login_url, headers=headers, data=parse.urlencode(data).encode("utf-8"), method="POST")
    opener.open(req)

def visit_profile(opener):
    # 2.访问个人主页

    # 获取个人主页的页面的时候， 不要新建一个opener
    # 而应该使用之前的那个opener, 因为之前的那个opener已经包含了
    # 登录所需要的cookie信息

    req = request.Request(url=dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as fp:
        '''
        write函数必须写入一个str数据类型
        resp.read()读出来是一个bytes数据类型
        bytes --> decode --> str
        str   --> encode -->bytes
        print()函数之后无法写入html
        '''
        fp.write(resp.read().decode('utf-8'))
        fp.close()

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
from urllib import request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

# 这个是没有使用代理的
resp = request.urlopen("http://httpbin.org/ip")
print(resp.read().decode("utf-8"))

# 这个是使用代理的
# 使用ProxyHandler,出入代理构建一个handler
handler = request.ProxyHandler({"http": "60.247.59.182:31204"})

# 使用handler构建一个opener
opener = request.build_opener(handler)

# 使用opener去发送一个请求
req = request.Request("http://httpbin.org/ip")
resp = opener.open(req)
print(resp.read().decode("utf-8"))

# 西刺免费代理ip http://www.xicidaili.com/
# 快代理 http://www.kuaidaili.com/
# 代理云 http://www.dailiyun.com/

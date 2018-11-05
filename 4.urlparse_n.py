from urllib import parse

url = "http://www.baidu.com/s?username=xiaoming"

result = parse.urlparse(url)
ret = parse.urlsplit(url)
print("urlparse出来的结果: %s" % str(result))
# urlparse出来的结果: ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='', query='username=xiaoming', fragment='')
print("scheme:%s" % ret.scheme)  # scheme:http
print("path:%s" % ret.path)  # path:/s
print("netloc:%s" % ret.netloc)  # query:username=xiaoming
print("query:%s" % ret.query)  # netloc:www.baidu.com

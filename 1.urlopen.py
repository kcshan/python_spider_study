from urllib import request

resp = request.urlopen("http://www.baidu.com")
print(resp.read()) # 全部读取
print(resp.read(10))
print(resp.readline())  # 读取单行
print(resp.readlines())  # 读取多行以列表的形式
print(resp.getcode())  # 获取状态码

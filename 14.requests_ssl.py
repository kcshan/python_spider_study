import requests

resp = requests.get("https://www.baidu.com/", verify=False)
print(resp.text)
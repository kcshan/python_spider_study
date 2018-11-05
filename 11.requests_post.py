import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


headers = {
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
data = {
    "first": "true",
    "pn": 1,
    "kd": "python"
}

resp = requests.post(url=url, params=data, headers=headers)
print(resp.json())
print(type(resp.json()))  # <class 'dict'>

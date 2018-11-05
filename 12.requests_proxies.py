import requests


url = "http://httpbin.org/ip"
proxy = {
    "http": "117.127.0.203:80"
}
resp = requests.get(url=url, proxies=proxy)
print(resp.text)
# {
#   "origin": "117.127.0.203"
# }

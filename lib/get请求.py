import requests
url='http://httpbin.org/get'
r=requests.get(url)
print(r.text)
print(r.content)
print(r.status_code)
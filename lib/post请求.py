import requests
url="http://httpbin.org/post"
headers={
    "content-type":"x-www-form-urlencoded"
}
data={
    "name":"xiaohong",
    "age":"11"
}
r=requests.post(url=url,headers=headers,data=data)
print(r.text)
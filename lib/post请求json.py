import requests
url="http://httpbin.org/post"
headers={
    "content-type":"x-www-form-urlencoded"
}
data='''{
    "name":"xiaohong",
    "age":"11"
}'''
'{"name":"xiaohong","age":11}'
r=requests.post(url=url,data=data)
print(r.text)
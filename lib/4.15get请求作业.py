import requests
# url="http://192.168.55.66/Home/Goods/search.html?q=%E6%89%8B%E6%9C%BA"
# r=requests.get(url)
# print(r.text)
url= "http://192.168.55.66/Home/Goods/search.html"
pama={
    "q":"手机"

}
r=requests.get(url,params=pama)
print(r.text)

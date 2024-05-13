import requests
class p2p_add():
    url = "http://192.168.55.31:8080/p2p_management/addProduct"
    headers = {
        "Content - Type": "application / json"
    }

    def addProduct(self,pnum,pname,plimit,an):

        data = {"proNum":pnum,"proName":pname,"proLimit":plimit,"annualized":an}
        r = requests.post(url=self.url, headers=self.headers, json=data)
        print(r.text)


if __name__ == '__main__':
    p=p2p_add()
    p.addProduct("111","111","111","111")
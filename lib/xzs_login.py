import requests
class xzs_login():
    url = "http://192.168.55.31:8000/api/user/login"
    headers = {
        "Content - Type": "application / json"
    }

    def login(self,us,ps):

        data = {"userName": us, "password": ps, "remember": False}
        r = requests.post(url=self.url, headers=self.headers, json=data)
        print(r.text)


if __name__ == '__main__':
    z=xzs_login()
    z.login("student","123456")

import json,ddt
import unittest,requests

from lib import read_excel


@ddt.ddt
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = read_excel.readexcel()
        cls.l = cls.r.excel_to_list("test_user_data.xlsx", "test_user_login")
    @ddt.data("login_ok","login_erro1","login_erro2","login_erro3")
    def test_login(self,name):
        t = self.r.get_test_data(self.l, name)
        # print(t)
        url = t.get("url")
        # print(url)
        data = t.get("args")
        d = json.loads(data)
        exp = t["expect_res"]
        # print(exp)
        req = requests.post(url, json=d)

        # print(req.text)
        self.assertIn(exp, req.text)


if __name__ == '__main__':
    unittest.main()

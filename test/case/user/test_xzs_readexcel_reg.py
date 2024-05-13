import json
import unittest,requests

from lib import read_excel
from db import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r= read_excel.readexcel()
        cls.l=cls.r.excel_to_list("test_user_data.xlsx","test_user_reg")
    def test_regok(self):
        reg1=self.r.get_test_data(self.l,"reg_ok")
        print(reg1)
        url=reg1.get("url")
        args=reg1.get("args")
        res=reg1.get("expect_res")
        a=json.loads(args)
        name=a.get("userName")
        if check_user(name):
            del_user(name)
        r=requests.post(url,json=a)
        self.assertIn(res, r.text)
        del_user(name)
    def test_regerro(self):
        reg1 = self.r.get_test_data(self.l, "reg_erro")
        print(reg1)
        url = reg1.get("url")
        args = reg1.get("args")
        res = reg1.get("expect_res")
        a = json.loads(args)
        r = requests.post(url, json=a)
        self.assertEqual(res, r.text)


if __name__ == '__main__':
    unittest.main()

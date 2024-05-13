import unittest
from test.case.user.test_user_reg1 import MyTestCase as regtest


class MyTestCase(unittest.TestCase):
    def test_suit(self):
        suit=unittest.TestSuite()
        suit.addTest(regtest("test_regok"))
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

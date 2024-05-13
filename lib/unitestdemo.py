import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_01(self):
        print("test01")
        self.assertEqual(True, True)

    def test_02(self):
        print("test02")
        self.assertIn('h','hello')
    def test_03(self):
        print("test03")
        self.assertIs(2.0,2/4)
    def test_04(self):
        print("test04")
        self.assertEqual(True, True)




if __name__ == '__main__':
    unittest.main()

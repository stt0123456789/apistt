import unittest
import p2padd
class MyTestCase(unittest.TestCase):
    p=p2padd.p2p_add()
    def test_addok(self):
        t=self.p.addProduct("111","111","111","111")
        print(t)





if __name__ == '__main__':
    unittest.main()
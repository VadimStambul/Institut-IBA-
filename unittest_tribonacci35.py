import unittest
from tribonacci_homework import trib


class MyTestCase(unittest.TestCase):
    def test_trib(self):
        new_trib = trib(35, c=1, p=0, pp=0)
        self.assertEqual(new_trib, 334745777)


if __name__ == '__main__':
    unittest.main()

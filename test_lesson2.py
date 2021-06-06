import unittest
from lesson2_homehork import big_side

class MyTestCase(unittest.TestCase):
    def test_big_side(self):
        side_square = big_side(1, 2, 0)
        self.assertEqual(side_square, None)


if __name__ == '__main__':
    unittest.main()


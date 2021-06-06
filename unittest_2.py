import unittest
import full_name

class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
            full_name.full_name('Stambul',
                                "Vadim",
                                "Anatolyevich"),
            "Stambul Vadim Anatolyevich"
        )


    def test_big(self):
        self.assertEqual(
            full_name.full_name("STAMBUL",
                                "VADIM",
                                "ANATOLYEVICH"),
            "Stambul Vadim Anatolyevich"
        )


    def test_small(self):
        self.assertEqual(
            full_name.full_name("stambul",
                                "vadim",
                                "anatolyevich"),
            "Stambul Vadim Anatolyevich"
        )


if __name__ == '__main__':
    unittest.main()

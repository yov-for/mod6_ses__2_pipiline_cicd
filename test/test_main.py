from my_app.main_v1 import add
import unittest

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

if __name__ == '__main__':
    unittest.main()
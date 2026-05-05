import unittest
from app.cart import count_items


class CountItemsTest(unittest.TestCase):
    def test_count_items(self):
        self.assertEqual(count_items(5), 5)
        self.assertEqual(count_items(0), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(count_items(-1), 5)


if __name__ == "__main__":
    unittest.main()

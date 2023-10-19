import unittest


class TestMinSquareSize(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(min_square_size(10, 2, 3), 6)
        self.assertEqual(min_square_size(5, 4, 5), 5)
        self.assertEqual(min_square_size(15, 1, 1), 15)

    def test_invalid_input(self):
        self.assertEqual(min_square_size(0, 2, 3), (-1, -1))
        self.assertEqual(min_square_size(10, 0, 3), (-1, -1))
        self.assertEqual(min_square_size(10, 2, 0), (-1, -1))
        self.assertEqual(min_square_size(10, 2, 3), -1, -1)
        self.assertEqual(min_square_size(10**13, 2, 3), (-1, -1))


if __name__ == '__main__':
    unittest.main()

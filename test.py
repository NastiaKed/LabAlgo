import unittest

from main import monotone

array = [1, 2, 3, 4, 5]
array_2 = [5, 4, 3, 2, 1]
array_3 = [1, 2, 2, 3, 2, 4]
array_4 = [5, 4, 3, 1, 4, 5]
array_6 = [2, 2, 2, 2, 8]
array_7 = [2, 2, 2, 2, -1]


class MyTestCase(unittest.TestCase):
    def test_ask(self):
        self.assertEqual(True, monotone(array))

    def test_desk(self):
        self.assertEqual(True, monotone(array_2))

    def test_desk_3(self):
        self.assertEqual(False, monotone(array_3))

    def test_ask2(self):
        self.assertEqual(True, monotone(array_4))

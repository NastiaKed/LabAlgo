import unittest

from main import TreeNode, sum_of_depths


class MyTestCase(unittest.TestCase):
    def test_example(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(6, sum_of_depths(root))

    def test_null(self):
        self.assertEqual(0, sum_of_depths(None))

    def test_only_left(self):
        root = TreeNode(10)
        root.left = TreeNode(8)
        root.left.left = TreeNode(6)
        root.left.left.left = TreeNode(4)
        self.assertEqual(6,sum_of_depths(root))


if __name__ == '__main__':
    unittest.main()

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(node: TreeNode) -> int:
    def calc_depth(node, depth=0):
        if node is None:
            return 0

        return depth + calc_depth(node.left, depth + 1) + calc_depth(node.right, depth + 1)

    return calc_depth(node)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(100)
root.right.right.right = TreeNode(100)

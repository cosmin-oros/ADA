# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_binary_tree(root, val):
    if not root:
        return TreeNode(val)

    if val <= root.val:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            insert_into_binary_tree(root.left, val)
    else:
        if root.right is None:
            root.right = TreeNode(val)
        else:
            insert_into_binary_tree(root.right, val)


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)


class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        # swap children
        t = root.left
        root.left = root.right
        root.right = t

        # invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = TreeNode(4)
insert_into_binary_tree(root, 2)
insert_into_binary_tree(root, 7)
insert_into_binary_tree(root, 1)
insert_into_binary_tree(root, 3)
insert_into_binary_tree(root, 6)
insert_into_binary_tree(root, 9)

sol = Solution()

root = sol.invertTree(root)
print_in_order(root)
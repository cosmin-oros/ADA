# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution(object):
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True

            if not (right > node.val > left):
                return False

            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))


bst = TreeNode(6)
insert_into_binary_tree(bst, 2)
insert_into_binary_tree(bst, 8)
insert_into_binary_tree(bst, 0)
insert_into_binary_tree(bst, 4)
insert_into_binary_tree(bst, 7)
insert_into_binary_tree(bst, 9)
insert_into_binary_tree(bst, 3)
insert_into_binary_tree(bst, 5)
sol = Solution()

print(sol.isValidBST(bst))
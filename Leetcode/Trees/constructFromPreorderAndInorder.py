# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
# is the inorder traversal of the same tree, construct and return the binary tree.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 20, 15, 7]
sol = Solution()
tree = sol.buildTree(preorder, inorder)
print_tree(tree)

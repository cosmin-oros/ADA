# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or
# may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(sol.diameterOfBinaryTree(root))
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with
# a value greater than X.
#
# Return the number of good nodes in the binary tree.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            # update maxVal
            maxVal = max(maxVal, node.val)
            # recursive dfs call on left and right subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)


sol = Solution()
bst = TreeNode(3)
bst.left = TreeNode(1)
bst.left.left = TreeNode(3)
bst.right = TreeNode(4)
bst.right.left = TreeNode(1)
bst.right.right = TreeNode(5)
print(sol.goodNodes(bst))

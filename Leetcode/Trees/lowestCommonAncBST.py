# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

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
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p > cur.val and q > cur.val:
                cur = cur.right
            elif p < cur.val and q < cur.val:
                cur = cur.left
            else:
                # if one of the values or both are equal if the val of the node then that node is the LCA
                return cur.val


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

print(sol.lowestCommonAncestor(bst, 2, 8))

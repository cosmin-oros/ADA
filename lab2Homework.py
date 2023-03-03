class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left:
                self._insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(val, node.right)
            else:
                node.right = Node(val)

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, node):
        if not node:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)

    def searchClosest(self, k):
        return self._searchClosest(self.root, k)

    # it recursively searches the left or right subtree depending on whether
    # k is less than or greater than the value of the current node
    def _searchClosest(self, node, k):
        if node is None:
            return None

        if node.val == k:
            return node

        elif k < node.val:
            left_closest = self._searchClosest(node.left, k)
            if left_closest is None or abs(left_closest.val - k) > abs(node.val - k):
                return node
            else:
                return left_closest
        else:
            right_closest = self._searchClosest(node.right, k)
            if right_closest is None or abs(right_closest.val - k) > abs(node.val - k):
                return node
            else:
                return right_closest

    def checkExistTwoNodesWithSum(self, s):
        seen = set()
        return self._checkExistTwoNodesWithSum(self.root, s, seen)

    # it adds the value of the current node to the set of seen values
    # and recursively searches the left and right subtrees
    def _checkExistTwoNodesWithSum(self, node, s, seen):
        if node is None:
            return False
        if s - node.val in seen:
            return True
        seen.add(node.val)
        return self._checkExistTwoNodesWithSum(node.left, s, seen) \
               or self._checkExistTwoNodesWithSum(node.right, s, seen)

    def printPathFromTo(self, node1, node2):
        if node1 is None or node2 is None:
            return
        if node1.val < node2.val:
            self._printPathFromTo(self.root, node1.val, node2.val)
        else:
            self._printPathFromTo(self.root, node2.val, node1.val)

    # if the value of the current node is between min and max we print it and then
    # recursively move to the left and right with updated values for min and max
    # if the value of the current node is smaller than the min we move to the
    # right (to a larger value), if it is larger than max we move to the left
    def _printPathFromTo(self, node, min_val, max_val):
        if node is None:
            return
        if min_val <= node.val <= max_val:
            print(node.val)
            self._printPathFromTo(node.left, min_val, node.val)
            self._printPathFromTo(node.right, node.val, max_val)
        elif node.val < min_val:
            self._printPathFromTo(node.right, min_val, max_val)
        else:
            self._printPathFromTo(node.left, min_val, max_val)


# IsPerfectlyBalanced - returns true if the BST is perfectly balanced #
# (A binary tree is said to be perfectly balanced if for every node,
# the number of nodes in its two subtrees differs by maximum 1).
# The function must do the check in O(n) time, where n is the number of nodes ! (every node has to be handled just once)
def IsPerfectlyBalanced(node):
    if node is None:
        return True
    left_subtree_size = count_nodes(node.left)
    right_subtree_size = count_nodes(node.right)

    # we recursively check if the left and right subtrees are perfectly balanced,
    # if the sizes of the left and right subtrees differ by at most 1
    if abs(left_subtree_size - right_subtree_size) <= 1 \
            and IsPerfectlyBalanced(node.left) \
            and IsPerfectlyBalanced(node.right):
        return True
    return False


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


#   6
#  / \
#  5  9
# /\  /
# 3 7 8

bst = BST()
bst.insert(6)
bst.insert(5)
bst.insert(9)
bst.insert(3)
bst.insert(7)
bst.insert(8)

print(IsPerfectlyBalanced(bst.root))
print(bst.searchClosest(6).val)
print(bst.checkExistTwoNodesWithSum(14))

print()

node1 = bst.root.left
node2 = bst.root.right

bst.printPathFromTo(node1, node2)

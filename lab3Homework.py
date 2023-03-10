import time


# AVL Tree Node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

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

    def height(self, node):
        if node is None:
            return 0
        return node.height

    # check the difference between the height of the left and the height of the right
    # if it's larger than 1 then it's not balanced
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        # insert smaller values to the left and larger ones to the right
        if node is None:
            return Node(val)
        elif val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)

        # left left case
        if balance > 1 and val < node.left.val:
            return self.rotate_right(node)

        # right right case
        if balance < -1 and val > node.right.val:
            return self.rotate_left(node)

        # left right case (left rotate node.right and right rotate node)
        if balance > 1 and val > node.left.val:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # right left case (right rotate node.right and left rotate node)
        if balance < -1 and val < node.right.val:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # make the right node the root node and put the initial root as the left of the new root
    # and make the left of the right of initial root the right of it
    def rotate_left(self, node):
        right_node = node.right
        right_left_node = right_node.left
        right_node.left = node
        node.right = right_left_node

        return right_node

    # make the left node the root node and put the initial root as the right of the new root
    # and make the right of the left of initial root the left of it
    def rotate_right(self, node):
        left_node = node.left
        left_right_node = left_node.right
        left_node.right = node
        node.left = left_right_node

        return left_node

    # print AVL tree
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)


avl_tree = AVL()

start = time.perf_counter_ns()
avl_tree.insert(4)
avl_tree.insert(9)
avl_tree.insert(2)
avl_tree.insert(7)
avl_tree.insert(13)
avl_tree.insert(3)
avl_tree.insert(5)
end = time.perf_counter_ns()

avl_tree.inorder_traversal(avl_tree.root)
print()
print("AVL Random values insertion time: ", end - start, "ns")
print()

avl_tree2 = AVL()

start = time.perf_counter_ns()
avl_tree2.insert(1)
avl_tree2.insert(2)
avl_tree2.insert(3)
avl_tree2.insert(4)
avl_tree2.insert(5)
avl_tree2.insert(6)
avl_tree2.insert(7)
end = time.perf_counter_ns()

avl_tree2.inorder_traversal(avl_tree2.root)
print()
print("AVL increasing order values insertion time: ", end - start, "ns")
print()

start = time.perf_counter_ns()
avl_tree2.search(7)
end = time.perf_counter_ns()

print()
print("AVL search time: ", end - start, "ns")
print()

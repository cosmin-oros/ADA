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


def createBalancedBSTfromSortedArray(array):
    if not array:
        return None

    mid = len(array) // 2
    root = Node(array[mid])
    root.left = createBalancedBSTfromSortedArray(array[:mid])
    root.right = createBalancedBSTfromSortedArray(array[mid+1:])

    return root


def isPostorderArray(array):
    if not array:
        return True

    root = array[-1]
    i = 0
    while i < len(array) - 1 and array[i] < root:
        i += 1

    for j in range(i, len(array) - 1):
        if array[j] < root:
            return False

    return isPostorderArray(array[:i]) and isPostorderArray(array[i:-1])


def printBST(root):
    if root is None:
        return
    printBST(root.left)
    print(root.val, end=" ")
    printBST(root.right)


array = [7, 3, 2, 5, 4, 1, 9, 6, 8]
array.sort()

root = createBalancedBSTfromSortedArray(array)

printBST(root)

print()

print(isPostorderArray(array))
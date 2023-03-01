class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_tree(node):
    if node:
        print_tree(node.left)
        print(node)
        print_tree(node.right)


def print_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val)
    else:
        print_leaf_nodes(root.left)
        print_leaf_nodes(root.right)



# Create a binary tree with root node 1
root = Node(1)

# Set the left and right children of the root node
root.left = Node(2)
root.right = Node(3)

# Set the left and right children of the left child of the root node
root.left.left = Node(4)
root.left.right = Node(5)

# Print the binary tree and its leaf nodes
print('Binary Tree:')
print_tree(root)
print('\nLeaf Nodes:')
print_leaf_nodes(root)
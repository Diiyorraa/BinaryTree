class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.left) + self.size(node.right) + 1

    def print(self, traversal_type):
        if traversal_type == "size":
            return self.size(self.root)


binaryTree = BinaryTree(1)
binaryTree.root.left = Node(2)
binaryTree.root.right = Node(3)
binaryTree.root.left.left = Node(4)
binaryTree.root.left.right = Node(5)
binaryTree.root.right.left = Node(6)
binaryTree.root.right.right = Node(7)
print(binaryTree.print("size"))

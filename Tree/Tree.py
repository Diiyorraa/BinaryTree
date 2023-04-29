class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder(self, start, traversal):
        if start:
            traversal = traversal + (str(start.val) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal = traversal + (str(start.val) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal = traversal + (str(start.val) + "-")
        return traversal

binaryTree = BinaryTree(1)
binaryTree.root.left = Node(2)
binaryTree.root.right = Node(3)
binaryTree.root.left.left = Node(4)
binaryTree.root.left.right = Node(5)
binaryTree.root.right.left = Node(6)
binaryTree.root.right.right = Node(7)
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

print(binaryTree.print_tree("preorder"))
print(binaryTree.print_tree("inorder"))
print(binaryTree.print_tree("postorder"))

class Queue(object):
    def __init__(self):
        self.items= []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].val
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "levelorder":
            return self.levelorder_print()

    def levelorder_print(self):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)
        traversal = ""
        while len(queue) >0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.print_tree("levelorder"))

# Reverse Level_Order
class Stack(object):
    def __init__(self):
        self.items = []
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self,item):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return  len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s = s+ str(self.items[i].val) + "-"
        return s


# Reverse Level_Order
class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s = s + str(self.items[i].val) + "-"
        return s


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def reverse_levelorder(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.val) + "-"
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "reverse_levelorder":
            return self.reverse_levelorder(self.root)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.print_tree("reverse_levelorder"))






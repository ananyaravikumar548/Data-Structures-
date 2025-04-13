from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

# 🔽 Usage
bt = BinaryTree()
for data in [1, 2, 3, 4, 5, 6, 7]:
    bt.insert(data)

print("In-order Traversal:")
bt.in_order_traversal(bt.root)

print("\nPre-order Traversal:")
bt.pre_order_traversal(bt.root)

print("\nPost-order Traversal:")
bt.post_order_traversal(bt.root)

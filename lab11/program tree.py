class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # 1. Insert data into the binary tree (simple level-order insertion)
    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            elif current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    # 2. Pre-order traversal
    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # 3. Find Lowest Common Ancestor (LCA)
    def find_lca(self, root, node1, node2):
        if root is None:
            return None
        if root.data == node1 or root.data == node2:
            return root

        left_lca = self.find_lca(root.left, node1, node2)
        right_lca = self.find_lca(root.right, node1, node2)

        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca

    # 4. Find grandchildren of a node
    def find_grandchildren(self, node_value):
        def find_node(root, value):
            if root is None:
                return None
            if root.data == value:
                return root
            left = find_node(root.left, value)
            if left:
                return left
            return find_node(root.right, value)

        target = find_node(self.root, node_value)
        grandchildren = []

        if target:
            children = [target.left, target.right]
            for child in children:
                if child:
                    if child.left:
                        grandchildren.append(child.left.data)
                    if child.right:
                        grandchildren.append(child.right.data)
        return grandchildren

# ----------------------------
# Example usage
tree = BinaryTree()
for value in [1, 2, 3, 4, 5, 6, 7]:
    tree.insert(value)

print("Pre-order Traversal:")
tree.pre_order_traversal(tree.root)

# Find LCA of 4 and 5
lca_node = tree.find_lca(tree.root, 4, 5)
print("\nLowest Common Ancestor of 4 and 5:", lca_node.data if lca_node else "Not Found")

# Find grandchildren of node 2
print("Grandchildren of node 2:", tree.find_grandchildren(2))

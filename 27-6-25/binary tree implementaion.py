class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

# Example usage:
bt = BinaryTree()
for val in [1, 2, 3, 4, 5, 6, 7]:
    bt.insert(val)

print("Preorder:")
bt.preorder(bt.root)

print("\nInorder:")
bt.inorder(bt.root)

print("\nPostorder:")
bt.postorder(bt.root)

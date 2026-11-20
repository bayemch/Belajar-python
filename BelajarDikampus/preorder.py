class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)

root.left = Node(30)
root.right = Node(70)


root.left.left = Node(20)
root.left.right = Node(30)

root.right.left = Node(60)
root.right.right = Node(80)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

preorder(root)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


inorder(root)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

postorder(root)
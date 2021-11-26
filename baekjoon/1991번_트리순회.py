class Node:
    def __init__(self, data, left_data, right_data):
        self.data = data
        self.left_data = left_data
        self.right_data = right_data

def preorder(node):
    print(node.data, end='')
    if node.left_data != ".":
        preorder(tree[node.left_data])
    if node.right_data != ".":
        preorder(tree[node.right_data])

def inorder(node):
    if node.left_data != ".":
        inorder(tree[node.left_data])
    print(node.data, end='')
    if node.right_data != ".":
        inorder(tree[node.right_data])

def postorder(node):
    if node.left_data != ".":
        postorder(tree[node.left_data])
    if node.right_data != ".":
        postorder(tree[node.right_data])
    print(node.data, end='')

n = int(input())
tree = {}
for i in range(n):
    data, left_data, right_data = input().split()
    tree[data] = Node(data, left_data, right_data)

#print(preorder(tree['A']) 하면 함수의 return 값인 None이 같이 출력됨
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

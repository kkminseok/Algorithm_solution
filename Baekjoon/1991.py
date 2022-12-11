def preorder(root):
    if root !='.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')


node_size = int(input())
tree = {}
for i in range(node_size):
    nodes = list(map(str, input().split(' ')))
    tree[nodes[0]]= [nodes[1],nodes[2]]

preorder('A')
print()
inorder('A')
print()
postorder('A')
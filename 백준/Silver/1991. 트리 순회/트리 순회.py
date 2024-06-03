import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
def pre(root): 
    if root != '.':
        print(root, end='')  
        pre(tree[root][0])
        pre(tree[root][1]) 
        
def inorder(root):
    if root != '.': 
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right

def post(root):
    if root != '.':
        post(tree[root][0])  # left
        post(tree[root][1])  # right
        print(root, end='')
pre('A')
print()
inorder('A')
print()
post('A')

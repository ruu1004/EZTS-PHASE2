class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #1st recur on left child
        printInorder(root.left)
        #then print the data of the node
        print(root.val,end=' ')
        #now recur on right child
        printInorder(root.right)
def printPostorder(root):
    if root:
        #first recur on the left child
        printPostorder(root.left)
        #now recur on right child
        printPostorder(root.right)
        #then print the data of the node
        print(root.val,end=' ')
def printPreorder(root):
    if root:
        #then print the data of the node
        print(root.val,end=' ')
        #first recur on the left child
        printPreorder(root.left)
        #now recur on right child
        printPreorder(root.right)
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("PRE-ORDER:")
printPreorder(root)
print()
print('IN-ORDER:')
printInorder(root)
print()
print("POST-ORDER:")
printPostorder(root)
print()


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

newBT = TreeNode('Drinks')

lc = TreeNode('Hot')
rc = TreeNode('Cold')
newBT.left_child = lc
newBT.right_child = rc

def preorder_traversal(ll):
    if not ll:
        return
    else:
        print(ll.data)
    preorder_traversal(ll.left_child)
    preorder_traversal(ll.right_child)

preorder_traversal(newBT)
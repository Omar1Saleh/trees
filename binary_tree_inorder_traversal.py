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


def inorder_traversal(ll):
    if not ll:
        return
    inorder_traversal(ll.left_child)
    print(ll.data)
    inorder_traversal(ll.right_child)


inorder_traversal(newBT)

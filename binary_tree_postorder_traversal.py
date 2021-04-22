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


def postorder_traversal(ll):
    if not ll:
        return
    postorder_traversal(ll.left_child)
    postorder_traversal(ll.right_child)
    print(ll.data)


postorder_traversal(newBT)

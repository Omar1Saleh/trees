class bst:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, new_node):
    if root_node.data is None:
        root_node.data = new_node
    elif new_node <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = bst(new_node)
        else:
            insert_node(root_node.left_child, new_node)
    else:
        if root_node.right_child is None:
            root_node.right_child = bst(new_node)
        else:
            insert_node(root_node.right_child, new_node)
    return 'node has been inserted!'


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left_child)
    print(root.data)
    inorder_traversal(root.right_child)


def preorder_traversal(root):
    if not root:
        return
    print(root.data)
    inorder_traversal(root.left_child)
    inorder_traversal(root.right_child)


def postorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left_child)
    inorder_traversal(root.right_child)
    print(root.data)


def seach_BST(tree, value):
    try:
        if value == tree.data:
            return 'found in root!!'
        elif value < tree.data:
            if tree.left_child.data == value:
                return 'found in left child !'
            else:
                seach_BST(tree.left_child, value)
        elif value > tree.data:
            if tree.right_child.data == value:
                return 'found in right child !'
            else:
                seach_BST(tree.right_child, value)
    except:
        return 'Value not found!'

def mini(tree):
    current = tree
    while(current.left_child is not None):
        current = current.left_child
    return current

def delete_node(tree, value):
    if tree is None:
        return tree
    if value < tree.data :
        tree.left_chile = delete_node(tree.left_child, value)
    elif value > tree.data:
        tree.right_chile = delete_node(tree.right_child, value)
    else:
        if tree.left_child is None :
            temp = tree.right_child
            tree = None
            return temp
        if tree.right_child is None :
            temp = tree.left_child
            tree = None
            return temp
        temp = mini(tree.right_child)
        tree.data = temp.data
        tree.right_child = delete_node(tree.right_child, temp.data)
    return tree


def delet_tree(tree):
    tree.data = None
    tree.left_child = None
    tree.right_child = None
    return 'tree deleted!'

new_Bst = bst()
print(insert_node(new_Bst, 70))
print(insert_node(new_Bst, 40))
print(insert_node(new_Bst, 90))
print(insert_node(new_Bst, 80))
print(insert_node(new_Bst, 30))
print(insert_node(new_Bst, 60))
print(insert_node(new_Bst, 10))


delete_node(new_Bst, 90)
inorder_traversal(new_Bst)

delet_tree(new_Bst)
inorder_traversal(new_Bst)
# print(seach_BST(new_Bst, 9))

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next


class Queue:

    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return 'The queue is empty!'
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node


class avl:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


def levelorder_traversal(ll):
    if not ll:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(ll)
        while not (customqueue.is_empty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if (root.value.left_child is not None):
                customqueue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                customqueue.enqueue(root.value.right_child)


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


def search_avl(tree, value):
    try:
        if value == tree.data:
            return 'found in root!!'
        elif value < tree.data:
            if tree.left_child.data == value:
                return 'found in left child !'
            else:
                search_avl(tree.left_child, value)
        elif value > tree.data:
            if tree.right_child.data == value:
                return 'found in right child !'
            else:
                search_avl(tree.right_child, value)
    except:
        return 'Value not found!'


def getHeight(root):
    if not root:
        return 0
    else:
        return root.height


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.left_child
    # after assigning the left subtree to the new root, we have to get rid of it, by the following statement which
    # only returns null because there is no right child
    disbalanceNode.left_child = disbalanceNode.left_child.right_child
    # now assigning the original old imbalanced root as the right child of the new root node after right rotation
    newRoot.right_child = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left_child), getHeight(disbalanceNode.right_child))
    newRoot.height = 1 + max(getHeight(newRoot.left_child), getHeight(newRoot.right_child))
    return newRoot


def leftRotate(disbalanceNode):
    # same concept as above method but in reverse directions
    newRoot = disbalanceNode.right_child
    disbalanceNode.right_child = disbalanceNode.right_child.left_child
    newRoot.left_child = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left_child), getHeight(disbalanceNode.right_child))
    newRoot.height = 1 + max(getHeight(newRoot.left_child), getHeight(newRoot.right_child))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left_child) - getHeight(rootNode.right_child)


def insertNode(root, value):
    if not root:
        return avl(value) # if not existed create and exit the method
    elif value < root.data: # if less create in left subtree
        root.left_child = insertNode(root.left_child, value) # if more create in right subtree
    else:
        root.right_child = insertNode(root.right_child, value)

    root.height = 1 + max(getHeight(root.left_child), getHeight(root.right_child))
    balance = getBalance(root) # decides the condition LL,LR,RR,RL
    if balance > 1 and value < root.left_child.data: # left left condition
        return rightRotate(root) # for LL its right rotate condition
    if balance > 1 and value > root.left_child.data: # Left Right condition
        root.left_child = leftRotate(root.left_child)
        return rightRotate(root)
    if balance < -1 and value > root.right_child.data: # RR condition
        return leftRotate(root)
    if balance < -1 and value < root.right_child.data: # RL condition
        root.right_child = rightRotate(root.right_child)
        return leftRotate(root)
    return root


def getMinValueNode(rootNode):
    if rootNode is None or rootNode.left_child is None:
        return rootNode
    return getMinValueNode(rootNode.left_child)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left_child = deleteNode(rootNode.left_child, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right_child = deleteNode(rootNode.right_child, nodeValue)
    else:
        # single child case
        if rootNode.left_child is None:
            temp = rootNode.right_child
            rootNode = None
            return temp
        elif rootNode.right_child is None:
            temp = rootNode.left_child
            rootNode = None
            return temp
        # two children case
        temp = getMinValueNode(rootNode.right_child) # helps find successor of node to be deleted in case of 2 children
        rootNode.data = temp.data
        rootNode.right_child = deleteNode(rootNode.right_child, temp.data) # after finding the successor , delete it
    rootNode.height = 1 + max(getHeight(rootNode.left_child), getHeight(rootNode.right_child))
    balance = getBalance(rootNode) # helps find the balance of edges, and hence decides the condition
    # LL condition
    if balance > 1 and getBalance(rootNode.left_child) >= 0:
        return rightRotate(rootNode)
    # RR condition
    if balance < -1 and getBalance(rootNode.right_child) <= 0:
        return leftRotate(rootNode)
    # LR condition
    if balance > 1 and getBalance(rootNode.left_child) < 0:
        rootNode.left_child = leftRotate(rootNode.left_child)
        return rightRotate(rootNode)
    # RL condition
    if balance < -1 and getBalance(rootNode.right_child) > 0:
        rootNode.right_child = rightRotate(rootNode.right_child)
        return leftRotate(rootNode)
    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None
    return "The AVL has been successfully deleted"


newAVL = avl(30)
newAVL = insertNode(newAVL, 25)
newAVL = insertNode(newAVL, 35)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 50)
newAVL = insertNode(newAVL, 60)
newAVL = insertNode(newAVL, 70)
newAVL = insertNode(newAVL, 65)

deleteNode(newAVL,20)
deleteNode(newAVL,65)

#deleteAVL(newAVL)
levelorder_traversal(newAVL)

print(deleteAVL(newAVL))
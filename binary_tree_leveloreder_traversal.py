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


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


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


def seachTree(ll, item):
    if not ll:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(ll)
        while not (customqueue.is_empty()):
            root = customqueue.dequeue()
            if root.value.data == item:
                return 'Success!'
            if (root.value.left_child is not None):
                customqueue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                customqueue.enqueue(root.value.right_child)
        return 'Not Found!'


def insert_node(tree, item):
    if not tree:
        newBT = TreeNode(item)
    else:
        customqueue = Queue()
        customqueue.enqueue(tree)
        while not (customqueue.is_empty()):
            root = customqueue.dequeue()
            if root.value.left_child is not None:
                customqueue.enqueue(root.value.left_child)
            elif root.value.left_child is None:
                lc = TreeNode(item)
                root.value.left_child = lc
            elif root.value.right_child is not None:
                customqueue.enqueue(root.value.right_child)
            elif root.value.right_child is None:
                rc = TreeNode(item)
                root.value.right_child = rc


def levelorder_deepest_node(ll):
    if not ll:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(ll)
        while not (customqueue.is_empty()):
            root = customqueue.dequeue()
            if (root.value.left_child is not None):
                customqueue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                customqueue.enqueue(root.value.right_child)
        deepest_node = root.value
        return deepest_node


def delete_depest(tree, deeppest_node):
    if not tree:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(tree)
        while not (custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.value is deeppest_node:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child == deeppest_node:
                    root.value.right_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.right_chil)
            if root.value.left_child:
                if root.value.left_child == deeppest_node:
                    root.value.left_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.left_child)


def delete_node(ll, item):
    if not ll:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(ll)
        while not (customqueue.is_empty()):
            root = customqueue.dequeue()
            if root.value.data == item:
                deepest = levelorder_deepest_node(ll)
                root.value.data = deepest.data
                delete_depest(ll, deepest)
            if root.value.left_child is not None:
                customqueue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                customqueue.enqueue(root.value.right_child)
        return 'Not Found!'


def delete_tree(ll):
    if not ll:
        return 'tree does not exist!'
    else:
        ll.data = None
        ll.left_child = None
        ll.right_child = None
        return 'tree deleted!'


newBT = TreeNode('Drinks')

lc = TreeNode('Hot')
newBT.left_child = lc
insert_node(newBT, 'Cold')
insert_node(newBT, 'Tea')
insert_node(newBT, 'Coffee')
insert_node(newBT, 'Soda')
insert_node(newBT, 'Fanta')
delete_node(newBT, 'Tea')
levelorder_traversal(newBT)
delete_tree(newBT)
levelorder_traversal(newBT)

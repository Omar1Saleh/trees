class BTree:

    def __init__(self, size):
        self.custom_list = size * [None]
        self.max_size = size
        self.last_used_index = 0

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return 'the tree is full!'
        else:
            self.custom_list[self.last_used_index + 1] = value
            self.last_used_index += 1
            return 'value inserted!'

    def search_method(self, value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == value.lower() :
                return 'Value exists at index:'+str(i)
        return 'Value is not in list!'

    def preorder_traversal(self, index):
        if index > self.last_used_index :
            return
        print(self.custom_list[index])
        self.preorder_traversal(index*2)
        self.preorder_traversal(index*2 + 1)

    def inorder_traversal(self, index):
        if index > self.last_used_index :
            return
        self.inorder_traversal(index*2)
        print(self.custom_list[index])
        self.inorder_traversal(index*2 + 1)

    def postorder_traversal(self, index):
        if index > self.last_used_index :
            return
        self.postorder_traversal(index*2)
        self.postorder_traversal(index*2 + 1)
        print(self.custom_list[index])

    def level_order(self, tree):
        if tree.last_used_index == 0:
            return 'tree does not exist!'
        for i in range(1,len(tree.custom_list)):
            if tree.custom_list[i] is not None:
                print(tree.custom_list[i])

    def delete_node(self, tree, value):
        for i in range(1,len(tree.custom_list)):
            if tree.custom_list[i] == value:
                tree.custom_list[i] = tree.custom_list[tree.last_used_index]
                tree.custom_list[tree.last_used_index] = None
                tree.last_used_index -= 1
                return 'item is deleted!'

    def delete_tree(self, tree):
        tree.custom_list = None
        tree.last_used_index=0
        return 'tree deleted!'


newBT = BTree(8)
print(newBT.insert_node('drinks'))
print(newBT.insert_node('hot'))
print(newBT.insert_node('cold'))
print(newBT.insert_node('tea'))
print(newBT.insert_node('coffee'))
#newBT.postorder_traversal(1)
newBT.level_order(newBT)
print(newBT.delete_node(newBT, 'tea'))
newBT.level_order(newBT)
print(newBT.delete_tree(newBT))
print(newBT.level_order(newBT))
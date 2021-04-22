class TreeNode:

    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self,  level=0):
        ret = "   " * level + str(self.data) +'\n'
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def add_nodes(self, TreeNode):
        self.children.append(TreeNode)

simple_tree = TreeNode('Drinks:', [])

cold = TreeNode('Cold', [])
pepsi = TreeNode('Pespi', [])
soda = TreeNode('Soda', [])
fanta = TreeNode('Fanta', [])
hot = TreeNode('Hot', [])
tea = TreeNode('Tea', [])
gtea = TreeNode('Green Tea', [])
btea = TreeNode('Black Tea', [])
coffe = TreeNode('Coffee', [])
Mcoffe = TreeNode('Mocha Coffee', [])
Bcoffe  = TreeNode('Brazilian Coffee', [])
tea.add_nodes(gtea)
tea.add_nodes(btea)
hot.add_nodes(tea)
hot.add_nodes(coffe)
cold.add_nodes(pepsi)
cold.add_nodes(soda)
cold.add_nodes(fanta)
coffe.add_nodes(Mcoffe)
coffe.add_nodes(Bcoffe)
simple_tree.add_nodes(cold)
simple_tree.add_nodes(hot)

print(simple_tree)

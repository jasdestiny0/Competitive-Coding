class node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None

class tree:
    def __init__(self, node=None):
        self.root=node

    def __inorder__(self, node):
        self.inorder(node.left)
        if node!=None:
            print(node.value)
        else:
            return
        self.inorder(node.right)
    
    def insert(self, node, val):
        if self.root==None:
            self.root=node(val)
            return

        if node.value>=val and node.right==None:
            node.right=node(val)
            return

        elif node.value>=val:
            self.insert(node.right, val)

        elif node.value<val and node.left==None:
            node.left=node(val)
            return

        else:
            self.insert(node.left, val)


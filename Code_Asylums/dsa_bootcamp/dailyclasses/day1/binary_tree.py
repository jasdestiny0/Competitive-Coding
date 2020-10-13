class tree:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None

    def inorder(self):
        if self.left!=None:
            self.left.inorder()
        print(self.value)
        if self.right!=None:
            self.right.inorder()
    
    def insert(self, val):
        if self.left==None and self.value>val:
            self.left=tree(val)
        elif self.value>val:
            self.left.insert(val)
        elif self.right==None and self.value<=val:
            self.right=tree(val)
        elif self.right<=val:
            self.right.insert(val)
t=tree(1)
while True:
    option=int(input())
    if option==1:
        n=int(input())
        t.insert(n)
        print("Printing the tree")
        t.inorder()
    if option==2:
        break


class node:
    def __init__(self,number):
        self.value=number
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
    
    def insert(self,number):
        if self.root==None:
            self.root=node(number)
        else:
            self.insertNode(self.root,number)
    
    def insertNode(self,n,number):
        if number<n.value:
            if n.left!=None:
                self.insertNode(n.left,number)
            else:
                n.left=node(number)
        if number>=n.value:
            if n.right!=None:
                self.insertNode(n.right,number)
            else:
                n.right=node(number)
    
    def inorder(self,n):
        if n!=None:
            self.inorder(n.left)
            print(n.value)
            self.inorder(n.right)
        else:
            return
    
    def preorder(self,n):
        if n!=None:
            print(n.value)
            self.preorder(n.left)
            self.preorder(n.right)
        else:
            return
    
    def postoder(self,n):
        if n!=None:
            self.preorder(n.left)
            self.preorder(n.right) 
            print(n.value)
        else:
            return

choice=0
t=tree()
while choice!=-1:
    print("Enter choice (1:insert|2:inorder|3:preorder|4:postorder|-1:Exit):")
    choice=int(input())
    if choice==1:
        print("Enter number to be added")
        t.insert(int(input()))
    elif choice==2:         
        print("Inorder")
        t.inorder(t.root)
    elif choice==3:
        print("Preorder")
        t.preorder(t.root)
    elif choice==4:
        print("Postorder")
        t.postoder(t.root)
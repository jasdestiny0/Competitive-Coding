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
        else:
            self.right.insert(val)

    def lowestCommonAncestor(self, x, y):
        node=self.helper(self, x, y)
        if type(node)!=int:
            return node.value
        else:
            return "Either one or neither nodes exist"

    def helper(self, node, x, y):
        sumVal=0
        if x==node.value or y==node.value:
            return 1
        
        s1=s2=0
        if node.left!=None:
            s1=self.helper(node.left, x, y)
        if node.right!=None:
            s2=self.helper(node.right, x, y)

        if type(s1)!=int:
            return s1
        elif type(s2)!=int:
            return s2
        elif s1+s2==2:
            return node
        else:
            return s1+s2

        
t=tree(50)
l=[17, 72, 12, 23, 54, 76, 9, 14, 19, 67]
for i in l:
    t.insert(i)
t.inorder()
while True:
    print("Enter option")
    option=int(input())
    if option!=0:
        x,y=[int(i) for i in input("Enter the two nodes").split(' ')]
        print(t.lowestCommonAncestor(x,y))
    else:
        break


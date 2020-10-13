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

    def leftview(self, currentDepth=1, exploredDepth=0):
        exploredDepth1=exploredDepth
        exploredDepth2=exploredDepth

        if self.left!=None:
            exploredDepth1=self.leftview(currentDepth+1,exploredDepth)
    
        if exploredDepth<currentDepth:
            exploredDepth+=1
        print(self.value)

        if self.right!=None:
            exploredDepth2=self.leftview(currentDepth+1, exploredDepth)

        return max(exploredDepth, exploredDepth1, exploredDepth2)
        

t=tree(8)
while True:
    print("Enter option")
    option=int(input())
    if option==1:
        print("Enter number")
        n=int(input())
        t.insert(n)
        print("Printing the tree")
        t.inorder()
    if option==2:
        t.leftview()
    if option==3:
        break


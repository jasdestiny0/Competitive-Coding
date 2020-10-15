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
        if exploredDepth<currentDepth:
            exploredDepth+=1
            print(self.value)

        if self.left!=None:
            exploredDepth=self.left.leftview(currentDepth+1,exploredDepth)

        if self.right!=None:
            exploredDepth=self.right.leftview(currentDepth+1, exploredDepth)

        return exploredDepth

    def calc_height(self, height=1):
        h1=height
        h2=height
        if self.left!=None:
            h1=self.left.calc_height(height+1)
        if self.right!=None:
            h1=self.right.calc_height(height+1)
        return max(h1,h2)

    def invert(self):
        if self!=None:
            self.left, self.right=self.right, self.left
        if self.left!=None:
            self.left.invert()
        if self.right!=None:
            self.right.invert()

    def printLeftBoundary(self):
        if self.left==None and self.right==None:
            return
        print(self.value)
        if self.left!=None:
            self.left.printLeftBoundary()
        elif self.right!=None:
            self.right.printLeftBoundary()
    
    def printLeaves(self):
        if self.left is None and self.right is None:
            print(self.value)
            return
        if self.left!=None:
            self.left.printLeaves()

        if self.right!=None:
            self.right.printLeaves()

    def printRightBoundary(self):
        if self.left==None and self.right==None:
            return
        
        if self.right!=None:
            self.right.printRightBoundary()
        elif self.left!=None:
            self.left.printRightBoundary()
        
        print(self.value)

    def printBoundary(self):
        print("left")
        self.printLeftBoundary()
        print("leaves")
        self.printLeaves()
        print("right")
        self.printRightBoundary()

        
t=tree(25)
while True:
    print("Enter option")
    option=int(input())
    if option==1:
        print("Enter number")
        n=int(input())
        t.insert(n)
        print("Printing the tree")
        t.inorder()
    elif option==2:
        print("Printing the left side only")
        t.leftview()
    elif option==3:
        print("Height of tree: ", t.calc_height())
    elif option==4:
        t.invert()
        print("Inverted tree")
        t.inorder()
    elif option==5:
        t.printBoundary()
    else:
        break


def leftview(self, currentDepth=1, exploredDepth=0):
    if exploredDepth<currentDepth:
        print(self.value)
        exploredDepth+=1
    
    if self.left!=None and self.left!=None:
        exploredDepth1=self.leftview(self.left, currentDepth+1,exploredDepth)
    
    if self.right!=None and self.right!=None:
        exploredDepth2=self.leftview(self.right, currentDepth+1, exploredDepth)

    return max(exploredDepth, exploredDepth1, exploredDepth2)

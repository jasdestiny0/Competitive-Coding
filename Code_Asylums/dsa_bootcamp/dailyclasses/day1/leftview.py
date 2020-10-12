def leftview(self, currentDepth=1, exploredDepth=0, node):
    if node is None:
        return exploredDepth

    if exploredDepth<currentDepth:
        print(node.value)
        exploredDepth+=1
    
    if node.left!=None:
        exploredDepth1=self.leftview(currentDepth+1,exploredDepth, node.left)
    
    if node.left!=None:
        exploredDepth2=self.leftview(currentDepth+1, exploredDepth, node.right)

    return max(exploredDepth, exploredDepth1, exploredDepth2)

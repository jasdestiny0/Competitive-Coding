#O(n) time and O(1) space
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    List=[0]
	findSolution(root,0,List)
	return List[0]

def findSolution(root,depth,List):
	if root==None:
		return 
	List[0]+=depth
	findSolution(root.left,depth+1,List)
	findSolution(root.right,depth+1,List)
	



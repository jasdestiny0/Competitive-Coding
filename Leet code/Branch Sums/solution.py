# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


		
def branchSums(root):
	List=[]
    findSolution(root,0,List)
	return List

def findSolution(root,Sum,List):
	if root.left!=None:
		findSolution(root.left,Sum+root.value,List)
	if root.right!=None:
		findSolution(root.right,Sum+root.value,List)
	elif root.left==None and root.right==None:
		List.append(Sum+root.value)
	

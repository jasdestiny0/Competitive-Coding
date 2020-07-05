# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree,greatest=float("inf"),smallest=float("-inf")):
	if tree is None:
		return True
	elif tree.value<smallest or tree.value>=greatest:
		return False
	
	a=validateBst(tree.left, tree.value,smallest)
	b=validateBst(tree.right,greatest,tree.value)
	return a and b
	
	
    

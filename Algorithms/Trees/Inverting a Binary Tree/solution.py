def invertBinaryTree(tree):
	if tree!=None:
		temp=tree.left
		tree.left=tree.right
		tree.right=temp
		invertBinaryTree(tree.left)
		invertBinaryTree(tree.right)
	return tree	
	

def inOrderTraverse(tree, array):
	if tree!=None:
		inOrderTraverse(tree.left,array)
		array.append(tree.value)
		inOrderTraverse(tree.right,array)
	return array

def preOrderTraverse(tree, array):
    if tree!=None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right,array)
	return array

def postOrderTraverse(tree, array):
    if tree!=None:
		postOrderTraverse(tree.left,array)
		postOrderTraverse(tree.right,array)
		array.append(tree.value)
	return array

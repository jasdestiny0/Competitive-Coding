def iterativeInOrderTraversal(tree, callback):
    current=tree
	stack=[]
	while True:
		if current!=None:
			stack.append(current)
			current=current.left
		elif stack:
			current=stack.pop()
			callback(current)
			current=current.right
		else:
			break
	
			
def iterativeInOrderTraversal(tree, callback):
    	previousNode=None
	currentNode=tree 
	while currentNode!=None:
		if previousNode==None or previousNode==currentNode.parent:
			if currentNode.left!=None:
				nextNode=currentNode.left
			else:
				callback(currentNode)
				nextNode=currentNode.right if currentNode.right!=None else currentNode.parent
		elif previousNode == currentNode.left:
			callback(currentNode)
			nextNode=currentNode.right if currentNode.right is not None else currentNode.parent
		else:
			nextNode=currentNode.parent
		previousNode=currentNode
		currentNode=nextNode
			
		
	
		
		
	
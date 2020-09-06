def minHeightBst(array):
	return doInsert(array,0,len(array)-1)

def doInsert(array,left,right):
	if left>right:
		return None
	else:
		mid=(left+right)//2
		node=BST(array[mid])
		node.left=doInsert(array,left,mid-1)
		node.right=doInsert(array,mid+1,right)
	return node

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

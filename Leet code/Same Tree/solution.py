def sameTree(arrayOne, arrayTwo):
	t1=tree()
	t2=tree()
	
	for i in arrayOne:
		t1.insert(t1.root,i)
	for i in arrayTwo:
		t2.insert(t2.root,i)
		
	return t1.checkSame(t1.root,t2.root)
	
class tree:
	def __init__(self):
		self.root=None
	
	def insert(self,n,number):
		if self.root==None:
			self.root=node(number)
		else:
			if number<n.value:
				if n.left==None:
					n.left=node(number)
				else:
					self.insert(n.left,number)
			else:
				if n.right==None:
					n.right=node(number)
				else:
					self.insert(n.right,number)
					
	def checkSame(self,n1,n2):
		if n1==None and n2==None:
			return True
		elif n1!=n2:
			return False
		return self.checkSame(n1.left,n2.left) and self.checkSame(n1.right,n2.right)
		
class node:
	def __init__(self, number):
		self.value=number
		self.right=None
		self.left=None


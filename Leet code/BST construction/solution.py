# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value<self.value:
			if self.left==None:
				self.left=BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right==None:
				self.right=BST(value)
			else:
				self.right.insert(value)
						
        return self

    def contains(self, value):
		if value<self.value:
			if self.left==None:
				return False
			else:
				return self.left.contains(value)
		elif value>self.value:
			if self.right==None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True
	
	
    def remove(self, value,parent=None):
		if value<self.value:
			self.left.remove(value,self)
		elif value>self.value:
			self.right.remove(value,self)
		
		else:
			if self.left is not None and self.right is not None:
				self.value =self.right.getMinValue()
				self.right.remove(self.value,self)
	
			elif parent is None:
				if self.left is not None:
					self.value=self.left.value
					self.right=self.left.right
					self.left=self.left.left
				elif self.right is not None:
					self.value=self.right.value
					self.right=self.right.right
					self.left=self.right.left
				else:
					pass
			elif parent.left==self:
				parent.left=self.left if self.left is not None else self.right
			elif parent.right==self:
				parent.right=self.left if self.left is not None else self.right
		return self
				
	
	def getMinValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMinValue()

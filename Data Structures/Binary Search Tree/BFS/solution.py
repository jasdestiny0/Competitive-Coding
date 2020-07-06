# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		kids=[]
		kids=self.children
		array.append(self.name)
		
		while len(kids)>0:
			grandKids=[]
			for i in kids:
				array.append(i.name)
				grandKids+=i.children
			kids=grandKids
		return array

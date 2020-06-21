# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
		
def findLoop(head):
	visited={}
	node=head
    while node!=None:
		try:
			if visited[node.value]==True:
				break
		except:
			visited[node.value]=True
			node=node.next
	return node
		
	

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
		
def findLoop(head):
	turtle=head.next.next
	hare=head.next
	while turtle!=hare:
		turtle=turtle.next.next
		hare=hare.next
	turtle=head
	while hare!=turtle:
		hare=hare.next
		turtle=turtle.next
	return hare
		
	

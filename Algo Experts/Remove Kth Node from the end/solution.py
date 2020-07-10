# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	count=0
	node1=head
	while count!=k:
		count+=1
		node1=node1.next
		if node1==None:
			head.value=head.next.value
			head.next=head.next.next
			return head
	node2=head
	while node1.next!=None:
		node1=node1.next
		node2=node2.next
	node2.next=node2.next.next
	return head
	

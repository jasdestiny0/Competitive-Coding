# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    node=head
	count=0
	while node!=None:
		count+=1
		node=node.next
	fromFront=count-k
	index=0
	if fromFront==0:
		head.value=head.next.value
		head.next=head.next.next
	else:
		node=head
		while index<fromFront-1:
			node=node.next
			index+=1
		node.next=node.next.next
	

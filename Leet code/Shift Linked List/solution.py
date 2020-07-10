def shiftLinkedList(head, k):
	listLength=1
	listTail=head
	while listTail.next!=None:
		listTail=listTail.next
		listLength+=1
		
	while k<0:
		k+=listLength
	if k>0:
		k=k%listLength
	elif k==0:
		return head
	
	node1=head
	count=0
	while count!=k:
		node1=node1.next
		count+=1
	node2=head
	while node1.next!=None:
		node1=node1.next
		node2=node2.next
		
	n=node2
	node1.next=head
	head=node2.next
	node2.next=None
	return head
	


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

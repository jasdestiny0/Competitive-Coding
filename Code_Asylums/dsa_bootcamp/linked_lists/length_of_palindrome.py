class linked_list:
    def __init__(self, node=None):
        self.root=node
    
    def insert(self, val):
        if self.root==None:
            self.root=node(val)
            return
        n=self.root
        while n.next!=None:
            n=n.next
        n.next=node(val)

    def printLl(self):
        print("Printing the linked list")
        n=self.root
        while n!=None:
            print(n.value)
            n=n.next

    #calculate chain length
    def turtle_and_hare(self):
        turtle=self.root
        hare=self.root.next
        count=1
        while turtle!=hare:
            count+=1
            turtle=turtle.next
            hare=hare.next.next
        return count    

class node:
    def __init__(self, val):
        self.value=val
        self.next=None



ll=linked_list()
ll.insert(5)
ll.insert(4)

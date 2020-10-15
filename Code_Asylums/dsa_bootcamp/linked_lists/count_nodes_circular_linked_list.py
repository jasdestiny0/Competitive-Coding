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

    def cirularify(self):
        n=self.root
        while n.next!=None:
            n=n.next
        n.next=self.root

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
ll.printLl()

while True:
    option=int(input("Enter option: "))
    if option==1:   
        number=int(input("Enter the number: "))
        ll.insert(number)
        ll.printLl()
    #forming circular linked list
    elif option==2:
        ll.cirularify()
    #calculating the length
    elif option==3:
        print(ll.turtle_and_hare())
    elif option==4:
        ll.printLl()
        break
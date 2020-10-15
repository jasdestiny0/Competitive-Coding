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

    def  remove_duplicates(self):
        n=self.root
        while n.next!=None:
            if n.value==n.next.value:
                n.next=n.next.next
                continue
            n=n.next
    
    def length_of_palindrome(self):
        if self.root.next==None:
            return 1
        prev=None
        n=self.root
        while n!=None:
            



class node:
    def __init__(self, val):
        self.value=val
        self.next=None


ll=linked_list()
while True:
    option=int(input("Enter option: "))
    if option==1:   
        number=int(input("Enter the number: "))
        ll.insert(number)
        ll.printLl()
    #forming circular linked list
    elif option==2:
        ll.remove_duplicates()
        ll.printLl()
    else:
        break

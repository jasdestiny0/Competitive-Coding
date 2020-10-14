class linked_list:
    def __init__(self, node=None):
        self.root=node
        self.tail=node
    
    def insert(self, val):
        if self.root==None:
            print("hello")
            n=node(val)
            self.root=n
            self.tail=n
            return
        n=self.root
        while n.next!=None:
            n=n.next
        print("print",self.root.value)
        m=node(val)
        n.next=m
        m.prev=n
        self.tail.value=m.value
        self.tail.next=m.next


    def printLl(self):
        print("Printing the linked list")
        n=self.root
        print("root ",n.value)
        while n!=None:
            print(n.value)
            n=n.next

    def printLlReverse(self):
        print("Printing the linked list reverse")
        n=self.tail
        while n!=None:
            print(n.value)
            n=n.prev

class node:
    def __init__(self, val):
        self.value=val
        self.next=None
        self.prev=None

ll=linked_list()

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
    elif option==5:
        ll.printLlReverse()
    else:
        break
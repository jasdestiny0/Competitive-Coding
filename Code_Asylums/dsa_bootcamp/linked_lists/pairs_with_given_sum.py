class linked_list:
    def __init__(self, node=None):
        self.root=node
        self.tail=node
    
    def insert(self, val):
        if self.root==None:
            n=node(val)
            self.root=n
            self.tail=n
            return
        n=self.root
        while n.next!=None:
            n=n.next
        m=node(val)
        n.next=m
        m.prev=n
        self.tail.value=m.value
        self.tail.next=m.next


    def printLl(self):
        print("Printing the linked list")
        n=self.root
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

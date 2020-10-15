class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self, val):
        if self.head==None:
            self.head=self.tail=node(val)
            return
        n=self.head
        while n.next!=None:
            n=n.next
        m=node(val)
        m.prev=n
        n.next=m
        self.tail=m
    
    def printLl(self):
        m=self.head
        while m!=None:
            print(m.value)
            m=m.next

    def printLlReverse(self):
        m=self.tail
        while m!=None:
            print(m.value)
            m=m.prev


class node:
    def __init__(self, val):
        self.value=val
        self.prev=None
        self.next=None

ll=linkedList()
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.printLl()
ll.printLlReverse()


print(ll.head.value, ll.tail.value)
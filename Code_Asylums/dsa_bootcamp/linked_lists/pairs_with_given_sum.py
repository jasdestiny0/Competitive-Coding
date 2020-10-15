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

    def pairsWithGivenSum(self, n):
        l=self.head
        r=self.tail
        solution=[]
        while l.value<=r.value:
            if (l.value+r.value)<n:
                l=l.next
            elif (l.value+r.value)>n:
                r=r.prev
            else:
                solution.append([r.value, l.value,])
                l=l.next
                r=r.prev
        return solution




class node:
    def __init__(self, val):
        self.value=val
        self.prev=None
        self.next=None

ll=linkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(8)
ll.insert(9)
print("Printing Linked List")
ll.printLl()
print("pairs with given sum")
print(ll.pairsWithGivenSum(7))

class node:
    def __init__(self,x):
        self.value=x
        self.next=None

class linkedList:
    def __init__(self,n=None):
        self.head=n

    def insert(self,n):
        if self.head==None:
            self.head=n
            return
        node=self.head
        if node==None:
            node=n
        while node.next!=None:
            node=node.next
        node.next=n

    def printL(self):
        node=self.head
        while node!=None:
            print(node.value)
            node=node.next
        print(' ')
        

    def delete(self, val):
        node=self.head
        if node.value==val:
            self.head=self.head.next
            return
        while node.next!=None:
            if node.next.value==val:
                node.next=node.next.next
                return
            node=node.next

class lrucache:
    def __init__(self,size=3):
        self.ll=linkedList()
        self.pageSize=size
        self.n=0
        self.hash={}

    def request(self,val):
        if val in self.hash:
            print("page hit")
            
        elif self.n +1 > self.pageSize:
            self.ll.delete(self.ll.head.value)
            n=node(val)
            self.ll.insert(n)
            self.hash[val]=True
            
        else:
            n=node(val)
            self.ll.insert(n)
            self.hash[val]=True
            self.n+=1
            
    def printlru(self):
        print(self.ll.printL())
        
        
l=lrucache(2)
l.request(1)

l.printlru()
l.request(2)

l.printlru()
l.request(3)

l.printlru()
l.request(4)

l.printlru()



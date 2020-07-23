class node:
    def __init__(self, value):
        self.value=value
        self.next=None

class linkedList:
    def __init__(self, node=None):
        self.head=node
        self.tail=node

    def insertAtEnd(self, value):
        newNode=node(value)
        if self.tail==None:
            self.tail=newNode
            self.head=newNode
            return 
        self.tail.next=newNode
        self.tail=newNode
    
    def insertAtTop(self, value):
        newNode=node(value)
        if self.head==None:
            print("halo")
            self.head=newNode
            self.tail=newNode
            return
        newNode.next=self.head
        self.head=newNode
    
    def printLL(self):
        if self.head==None:
            return
        newNode=self.head
        while(newNode!=None):
            print(newNode.value)
            newNode=newNode.next
    
    def delete(self, number):
        if self.head.value==number:
            self.head=self.head.next
            return
        
        prevNode=self.head
        nextNode=self.head.next
        while nextNode!=None:
            if nextNode.value==number:
                prevNode.next=nextNode.next
            prevNode=prevNode.next
            nextNode=nextNode.next

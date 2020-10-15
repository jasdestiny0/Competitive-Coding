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

    def calcMaxLen(self, a, b):
        len=0
        while a!=None and b!=None:
            if a.value==b.value:
                len+=1
            else:
                break
            a=a.next
            b=b.next
        return len
    
    def length_of_palindrome(self):
        if self.root.next==None:
            return 1
        prev=None
        n=self.root
        maxlen=currlen1=currlen2=1
        while n!=None:
            temp=n.next
            n.next=prev
            prev=n
            n=temp
            if n!=None:
                currlen1=2*self.calcMaxLen(temp, n)
            else:
                break

            if n.next!=None:
                currlen2=(2*self.calcMaxLen(temp, n.next))+1
            maxlen=max(maxlen, currlen1, currlen2)
        self.root=prev
        return maxlen



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

    elif option==3:
        print(ll.length_of_palindrome())
    else:
        break

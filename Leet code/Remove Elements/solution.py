# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        head=self.remove(head, val)
        return head
    
    def remove(self, head, value):
        if head==None:
            return
        prev=head
        n=head.next
        while n!=None:
            if n.val==value:
                prev.next=n.next
                n=n.next
                continue
            n=n.next
            prev=prev.next
        if head.val==value:
            head=head.next
        return head
        
        

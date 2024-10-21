# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        curr= head
        l = 0
        while curr:
            l+=1
            curr = curr.next
        if l==n:
            head = head.next
            return head
        curr= head

        for i in range(l-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head        
        

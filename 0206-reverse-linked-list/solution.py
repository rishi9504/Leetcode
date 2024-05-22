# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        c,n = head,head.next
        c.next=None
        while n is not None:
            nn = n.next
            # print(c)
            n.next = c
            c = n
            n = nn
        return c
        
        
        

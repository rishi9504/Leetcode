# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a,b = head, head
        while b and b.next:
            a=a.next
            b=b.next.next
            if a == b:
                b = head
                while b!=a:
                    a = a.next
                    b=b.next
                return b    

        return None
        

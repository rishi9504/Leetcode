# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        l =1
        cur = head
        # count length of ll
        while cur.next:
            cur = cur=cur.next
            l+=1
            
        tail = cur
        k = k% l
        if k==0:
            return head
        new_tail = head
        for i in range(l-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head                
        

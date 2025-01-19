# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev,curr = None,slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev=curr
            curr=temp
        ms=0
        f,s = head,prev
        while s:
            ms = max(ms,f.val+s.val)
            f = f.next
            s=s.next
        return ms            
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=1
        h,c,fs,ls=head,head,None,None
        while c:
            if l==k:
                fs=c
            l+=1
            c=c.next
        c=head
        for i in range(l-k-1):
            c=c.next
        ls=c
        fs.val,ls.val=ls.val,fs.val
        return head

        

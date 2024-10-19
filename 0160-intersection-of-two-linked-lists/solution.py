# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1!=l2:  
            if l1: 
                l1=l1.next 
            else:
                l1 = headB 
            if l2:  
                l2=l2.next 
            else:
                l2 = headA 
        return l1 

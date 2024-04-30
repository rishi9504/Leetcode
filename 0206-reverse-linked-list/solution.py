# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #setting a prev node
        prev = None
        #setting current node to head
        current = head
        # loop for finding the last element, once found set the next to last node
        # now move back linking the elements backwards using the pointer
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
        
        

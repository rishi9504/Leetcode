# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(h):
            if not h or not h.next:
                return h
            f,s=h,h.next
            f.next=swap(s.next)
            s.next=f
            return s
        # nh = head
        return swap(head)
        # return nh
#         We define the function to implement as swap(head), where the input parameter head refers to the head of a linked list. The function should return the head of the new linked list that has any adjacent nodes swapped.

# Following the guidelines we lay out above, we can implement the function as follows:

# First, we swap the first two nodes in the list, i.e. head and head.next;
# Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
# Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.


        
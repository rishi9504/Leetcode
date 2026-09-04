# 83. Remove Duplicates from Sorted List
# Solved
# Easy

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
#  Return the linked list sorted as well.


# This function removes duplicates from a sorted linked list. 
# It iterates through the list, and if a node's value is the same as the next node's value, 
# it skips the next node by linking the current node to the node after the next node.
# If the values are different, it moves to the next node. 
# The function returns the head of the modified list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c= head
        while c and c.next:
            if c.val==c.next.val:
                c.next=c.next.next
            else:
                c = c.next
        return head
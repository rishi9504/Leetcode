# 2095. Delete the Middle Node of a Linked List
# Solved
# Medium

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Here's a step-by-step breakdown of how the code works:

# 1. It checks if the `head` is `None`. If it is, the method returns `None`.

# 2. It creates a new `ListNode` called `prev` with a value of `0` and 
# sets its `next` pointer to the `head` of the linked list.

# 3. It sets `slow` to `prev` and `fast` to the `head`.

# 4. It enters a loop that continues until `fast` is `None` or `fast.next` is `None`.

# 5. In each iteration of the loop, it moves `slow` to the next node and `fast` 
# to the next node's next node.

# 6. After the loop, it sets `slow.next` to the node after the node pointed to by `slow`.

# 7. Finally, it returns the `next` pointer of `prev`, which is the modified linked list.

# In summary, this code snippet deletes the middle node of a linked list.

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return prev.next        
        
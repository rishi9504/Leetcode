# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while head1 is not None or head2 is not None or carry != 0:
            x = head1.val if head1 is not None else 0
            y = head2.val if head2 is not None else 0
            sum = carry + x + y
            carry = 1 if sum > 9 else 0
            current.next = ListNode(sum % 10)
            current = current.next
            if head1 is not None:
                head1 = head1.next
            if head2 is not None:
                head2 = head2.next
        return dummyHead.next
            

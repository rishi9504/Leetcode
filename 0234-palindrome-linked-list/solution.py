# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        rev = None                      # head of the already-reversed part

        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = rev
            rev = slow
            slow = next_slow

        # if fast is not null, slow is middle element of odd length list which is skipped
        # if fast is null, slow is first element of 2nd half of even length list
        if fast:
            slow = slow.next

        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next

        return True

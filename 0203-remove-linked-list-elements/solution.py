# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # h=head
        # if not head:
        #     return None
        # while h and h.val==val:
        #     h=h.next
        # while h:
        #     if h.next:
        #         if h.next.val == val:
        #             h.next=h.next.next
        #         h=h.next
        #     else:
        #         h=h.next

        # return head
        while head and head.val == val:
            head = head.next
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:    
                curr = curr.next
        return head            

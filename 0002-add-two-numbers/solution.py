# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = ListNode()
#         head = cur
#         c = 0
#         while l1 is not None or l2 is not None or c != 0:
#             n1 = l1.val if l1 is not None else 0
#             n2 = l2.val if l2 is not None else 0
#             s = n1+n2+c
#             print(n1,n2,c,s)
#             n = s%10
#             c = s//10
#             # c,n = divmod(s,10)
#             # if l1.next is None or l2.next is None:
#             #     break
#             _next = ListNode(n)
#             head.next = _next
#             cur = head.next
#             l1=l1.next if l1 is not None else None
#             l2=l2.next if l2 is not None else None
#         # while l1 is not None or l2 is not None:
#         # res = cur.next
#         res = cur.next
#         cur.next = None



#         return res


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result

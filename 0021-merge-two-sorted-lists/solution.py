# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # out =[]
        # i,j = 0,0
        # while i<len(list1) and j<len(list2):
        #     if list1[i]<list2[j]:
        #         out.append(list1[i])
        #         i+=1
        #     else:
        #         out.append(list2[j])
        #         j+=1
        # while i<len(list1):
        #     out.append(list1[i])
        #     i+=1
        # while j<len(list2):
        #     out.append(list2[j])
        #     j+=1
        p = d = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return d.next        


        

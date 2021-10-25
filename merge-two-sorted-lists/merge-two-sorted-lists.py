# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        flag1, flag2 = False, False
        for _ in range(50):
            if l1 is None:
                flag1 = True
            else:
                l.append(l1.val)
                l1 = l1.next  
                
            if l2 is None:
                flag2 = True
            else:
                l.append(l2.val)
                l2 = l2.next
                
            if flag1 and flag2:
                break
                
        l.sort(reverse=True)
        l_ = None
        for v in l:
            temp = ListNode(v)
            temp.next = l_
            l_ = temp
        return l_
    
#         if l1 is None :
#             return l2
#         if l2 is None :
#             return l1
#         if (l1.val > l2.val) :
#             head = ListNode(l2.val)
#             head.next = self.mergeTwoLists(l1, l2.next)
#         else :
#             head = ListNode(l1.val)
#             head.next = self.mergeTwoLists(l1.next, l2)

#         return head
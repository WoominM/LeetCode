# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i ,num = 0, 0
        while l1 or l2:
            if l1:
                num += l1.val * 10 ** i
                l1 = l1.next
            if l2:
                num += l2.val * 10 ** i
                l2 = l2.next
            i += 1
            
        num = str(num)
        output = None
        for n in num:
            output = ListNode(n, output)
        return output
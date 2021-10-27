# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        dic = {}
        while True:
            if head.next:
                if head.next.val in dic.keys() and dic[head.next.val] == head.next.next:
                    return True
                else:
                    dic[head.val] = head.next
                    head = head.next
            else:
                return False
            
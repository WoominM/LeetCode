# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            if not head:
                return
            
            self.out = ListNode(head.val, self.out)
            helper(head.next)
            
        
        self.out = None
        helper(head)
        return self.out
            
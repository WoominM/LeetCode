# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        # def helper(head, revlist=None):
        #     if not head:
        #         return revlist
        #     return helper(head.next, ListNode(val=head.val, next=revlist))
        # return helper(head)
    
        revlist = None
        while head:
            revlist = ListNode(val=head.val, next=revlist)
            head = head.next
        return revlist
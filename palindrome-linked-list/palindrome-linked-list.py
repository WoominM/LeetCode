# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def helper(head, revlist=[]):
            if not head:
                return True if list(reversed(revlist)) == revlist else False
            revlist.append(head.val)
            return helper(head.next, revlist) 
        
        return helper(head)
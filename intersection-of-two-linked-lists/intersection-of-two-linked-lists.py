# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:       
            
#         self.lenA = 0
#         nodeA = headA
#         while nodeA:
#             self.lenA += 1
#             nodeA = nodeA.next
            
#         self.lenB = 0
#         nodeB = headB
#         while nodeB:
#             self.lenB += 1
#             nodeB = nodeB.next
            
#         def helper(headA, headB, lenA, lenB):
#             if not headA or not headB or lenA < lenB:
#                 return None
#             elif headA == headB:
#                 return headB
#             lenA -= 1
#             return helper(headA.next, headB, lenA, lenB)
        
#         def helper2(headA, headB, lenA, lenB):
#             if headB is None:
#                 return None
#             if lenA >= lenB:
#                 itnode = helper(headA, headB, lenA, lenB)
#                 if itnode is not None:
#                     return itnode
#             lenB -= 1
#             return helper2(headA, headB.next, lenA, lenB) 
            
#         return helper2(headA, headB, self.lenA, self.lenB)    
    
    
    
#         def compare(headA, headB):
#             while headA:
#                 if headA == headB:
#                     return headA
#                 headA = headA.next
#                 headB = headB.next
#             return None
        
#         if self.lenA > self.lenB:
#             for i in range(self.lenA - self.lenB):
#                 headA = headA.next
#         else:
#             for i in range(self.lenB - self.lenA):
#                 headB = headB.next
                
#         return compare(headA, headB)

        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
    
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p, q = root, root
        que = deque([(p, q)])
        while que:
            p, q = que.popleft()
            if not self.check(p, q):
                return False
            if p:
                que.append((p.left, q.right))
                que.append((p.right, q.left))
        return True
            
    def check(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False   
        return True

        
        
### recursively
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return self.helper(root, root)
        
#     def helper(self, p, q):
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False        
#         return self.helper(p.left, q.right) and self.helper(p.right, q.left)
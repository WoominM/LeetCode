# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root):
            if self.out != -1:
                return
            if not root:
                return
            
            if not (p.val > root.val and q.val > root.val) and \
                not (p.val < root.val and q.val < root.val):
                self.out = root
            
            helper(root.left)
            helper(root.right)
        
        self.out = -1
        helper(root)
        return self.out
        
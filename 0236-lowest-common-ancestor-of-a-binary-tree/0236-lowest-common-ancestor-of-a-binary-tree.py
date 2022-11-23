# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            num_a = left + right
            if root.val == p.val or root.val == q.val:
                num_a += 1
            if num_a == 2 and self.out == -1:
                self.out = root
            return num_a
        
        self.out = -1
        helper(root)
        return self.out
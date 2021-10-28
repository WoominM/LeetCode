# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        
        self.depth = 0 
        self.maxdepth = 0
        if not root:
            return self.maxdepth
        
        def helper(node):
            if node is None:
                return
            
            self.depth += 1  
            
            if self.depth > self.maxdepth:
                self.maxdepth = self.depth
                
            helper(node.left)
            helper(node.right)
            self.depth -= 1
            
            return
        
        helper(root)
        return self.maxdepth
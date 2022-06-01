# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        self.depth = 0
        self.max = 0
        self.helper(root)
        return self.max
    
    def helper(self, root):
        if root:
            self.depth += 1
            if self.depth > self.max:
                self.max = self.depth
            self.helper(root.left)
            self.helper(root.right)
            self.depth -= 1
            
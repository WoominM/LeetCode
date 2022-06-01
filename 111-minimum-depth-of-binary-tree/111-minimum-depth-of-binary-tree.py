# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        self.depth = 0
        self.mindepth = 10001
        self.helper(root)
        return self.mindepth
    
    def helper(self, root):
        if root:
            self.depth += 1
            if not root.left and not root.right:
                if self.mindepth > self.depth:
                    self.mindepth = self.depth
            self.helper(root.left)
            self.helper(root.right)
            self.depth -= 1
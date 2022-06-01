# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)
        
    def helper(self, root):
        if root:
            if abs(self.maxDepth(root.left)-self.maxDepth(root.right)) > 1:
                return False
            return self.helper(root.left) and self.helper(root.right)
        return True
        
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
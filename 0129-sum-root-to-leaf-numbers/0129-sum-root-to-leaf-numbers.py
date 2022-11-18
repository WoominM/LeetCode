# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, sumv):
            sumv_ = sumv * 10 + int(root.val)
            if not root.left and not root.right:
                out.append(sumv_)
                return 
            
            if root.left:
                helper(root.left, sumv_)
            if root.right:
                helper(root.right, sumv_)
        
        out = []
        helper(root, 0)
        return sum(out)
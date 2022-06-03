# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         self.result = []
#         self.isleaf = []
#         self.sumvalue = 0
#         self.helper(root)
#         self.result = [self.result[i] if self.isleaf[i]!=-1 else -1001 for i in range(len(self.result))]
#         return targetSum in self.result
            
#     def helper(self, root):
#         if root:
#             self.sumvalue += root.val
#             self.result.append(self.sumvalue)
#             self.isleaf.append(1 if not root.left and not root.right else -1)
#             self.helper(root.left)
#             self.helper(root.right)
#             self.sumvalue -= root.val
            
            
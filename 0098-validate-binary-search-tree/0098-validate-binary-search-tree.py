# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, valid):
            if not root:
                return
            if root.val >= valid[1] or root.val <= valid[0]:
                self.isBST = False
                return
            
            helper(root.left, [valid[0], min(root.val, valid[1])])
            helper(root.right, [max(root.val, valid[0]), valid[1]])
        
        self.isBST = True
        helper(root, [-float('inf'), float('inf')])
        return self.isBST
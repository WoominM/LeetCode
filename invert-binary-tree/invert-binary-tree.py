# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root, ivttree=None):
            if not root:
                return 
            ivttree = TreeNode(root.val)
            ivttree.right = helper(root.left, ivttree.right)
            ivttree.left = helper(root.right, ivttree.left)
            return ivttree
        
        return helper(root)
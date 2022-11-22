# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return isSametree(root1.left, root2.left) and\
                    isSametree(root1.right, root2.right)
        
        def helper(root):
            if self.isST:
                return
            if not root:
                return
            if root.val == subRoot.val:
                if isSametree(root, subRoot):
                    self.isST = True
                    return
            
            helper(root.left)
            helper(root.right)
        
        self.isST = False
        helper(root)
        return self.isST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, depth):
            if not root:
                return
            if depth > self.max_depth:
                out.append(root.val)
                self.max_depth = depth
            
            helper(root.right, depth + 1)
            helper(root.left, depth + 1)
        
        out = []
        self.max_depth = 0
        helper(root, 1)
        return out
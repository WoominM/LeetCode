# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, deg):
            if not root:
                return
            level[deg].append(root.val)            
            helper(root.left, deg + 1)
            helper(root.right, deg + 1)
        
        level = collections.defaultdict(list)
        helper(root, 0)
        return list(level.values())
            
                
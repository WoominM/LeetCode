# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
### iteratively
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        it = []
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            it.append(root.val)
            root = root.right
        return it
                
### recursively
#     def inorderTraversal1(self, root):
#         it = []
#         self.helper(root, it)
#         return it

#     def helper(self, root, it):
#         if root:
#             self.helper(root.left, it)
#             it.append(root.val)
#             self.helper(root.right, it)
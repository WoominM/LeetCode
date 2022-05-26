# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        stack = []
        it = []
        mroot = root
        while stack or mroot is not None:
            while mroot is not None:
                stack.append(mroot)
                mroot = mroot.left
            mroot = stack.pop()
            it.append(mroot.val)
            mroot = mroot.right
        return it
                
    
        
### recursive approach

#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root == None:
#             return
#         self.it = []        
#         return self.dfs(root)
    
#     def dfs(self, root):
#         if root.left == None:
#             self.it.append(root.val)
#         else:
#             self.dfs(root.left)
#             self.it.append(root.val)
#         if root.right == None:
#             return self.it
#         self.dfs(root.right)
#         return self.it
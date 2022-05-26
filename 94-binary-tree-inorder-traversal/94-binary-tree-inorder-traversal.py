# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.it = []
        self.visited = [False] * 101
        self.n = 0
        if root == None:
            return
        return self.dfs(root, self.it)
    
    def dfs(self, root, it):
        if root.left == None:
            it.append(root.val)
        else:
            self.dfs(root.left, it)
            it.append(root.val)
        if root.right == None:
            return it
        self.dfs(root.right, it)
        return it
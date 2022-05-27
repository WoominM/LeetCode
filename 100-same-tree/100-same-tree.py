# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1, stack2 = [], []
        inf = 10001
        self.helper(p, stack1)
        self.helper(q, stack2)
        return stack1 == stack2
            
        
    def helper(self, tree, stack):
        if tree:
            stack.append(tree.val)
            self.helper(tree.left, stack)
            self.helper(tree.right, stack)
        else:
            stack.append(inf)
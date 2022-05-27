# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
### iterateively
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False
        stack1, stack2 = [], []
        while (stack1 and stack2) or (p and q):
            while p and q:  
                if p.val != q.val:
                    return False
                stack1.append(p)
                stack2.append(q)
                p, q = p.left, q.left
            if (not p and q) or (p and not q):
                return False
            p, q = stack1.pop(), stack2.pop()
            p, q = p.right, q.right
        if (not p and q) or (p and not q):
            return False    
        return True
     
        
        
### recursively1         
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     if not q or not p:
    #         return False
    #     if p.val != q.val:
    #         return False
    #     return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
### recursively2        
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #         stack1, stack2 = [], []
    #         inf = 10001
    #         self.helper(p, stack1)
    #         self.helper(q, stack2)
    #         return stack1 == stack2
    #     def helper(self, tree, stack):
    #         if tree:
    #             stack.append(tree.val)
    #             self.helper(tree.left, stack)
    #             self.helper(tree.right, stack)
    #         else:
    #             stack.append(inf)
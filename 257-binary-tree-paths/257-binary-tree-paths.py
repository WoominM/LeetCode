# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, teststr, out):
            if root:
                teststr += str(root.val)
                if root.left or root.right:
                    teststr += '->'
                helper(root.left, teststr, out)
                helper(root.right, teststr, out)
                if not root.left and not root.right:
                    out.append(teststr)
                    teststr = []        
        teststr, out = '', []
        helper(root, teststr, out)
        return out
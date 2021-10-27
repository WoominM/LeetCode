# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        
        if not root:
            return path
        elif root.left is None and root.right is None:
            return [root.val]        
        else:
            initnode = root
            dic = {}
            while True:
                if root.left is None:                
                    if root is initnode and initnode in dic.values():
                        return path
                    elif root.right is None:
                        path.append(root.val)
                        root = dic[root]                           
                    else:
                        if root.right not in dic.keys():
                            path.append(root.val)
                            dic[root.right] = root       
                            root = root.right
                        else:
                            root = dic[root]
                else:
                    if root.left in dic.keys():
                        path.append(root.val)
                        if root.right is None:
                            if root is initnode:
                                return path
                            root = dic[root]
                        else:
                            if root.right in dic.keys():
                                path.pop()
                                if root is initnode:
                                    return path
                                root = dic[root]
                            else:
                                dic[root.right] = root
                                root = root.right
                    else:
                        dic[root.left] = root
                        root = root.left
            
                
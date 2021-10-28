# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def sort2bst(nums):
            if not nums:
                return
            
            center = len(nums) // 2
            centernode = nums[center]
            root = TreeNode(centernode)
            root.left = sort2bst(nums[:center])
            root.right = sort2bst(nums[center+1:])

            return root
        
        return sort2bst(nums)
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

            center = nums[len(nums) // 2]
            root = TreeNode(center)
            root.left = sort2bst(nums[:len(nums) // 2])
            root.right = sort2bst(nums[len(nums) // 2 + 1:])

            return root
        
        return sort2bst(nums)
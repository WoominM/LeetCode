class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:  
        def helper(nums, target, path):
            if target == 0:
                out.append(path)
                return
            if target < 0:
                return
            
            for i in range(len(nums)):
                helper(nums[i:], target - nums[i], path + [nums[i]])
                
        out = []        
        helper(candidates, target, [])
        return out
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(path):
            if path == target:
                return 1
            elif path > target:
                return 0
            
            out = 0
            for num in nums:
                out += helper(path + num)
            return out
        
        return helper(0)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(visited, path):
            if len(path) == n:
                out.append(path)
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    helper(visited, path + [num])
                    visited.remove(num)
        
        out = []
        n = len(nums)
        helper(set(), [])
        return out

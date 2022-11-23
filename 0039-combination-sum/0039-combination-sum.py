class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(target, path, k):
            if target < 0:
                return
            if target == 0:
                out.append(path)
                return
            
            for i, num in enumerate(candidates[k:]):
                helper(target - num, path + [num], k + i)
        
        out = []
        visited = set()
        for i, num in enumerate(candidates):
            helper(target - num, [num], i)
        return out
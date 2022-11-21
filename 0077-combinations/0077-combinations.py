class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(start, path):
            if len(path) == k:
                out.append(path)
                return
            
            for i in range(start+1, n-k+len(path)+2):
                helper(i, path + [i])
        
        out = []
        for i in range(1, n-k+2):
            helper(i, [i])
        return out
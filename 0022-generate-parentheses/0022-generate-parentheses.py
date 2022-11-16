class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(len1, len2, path):
            if len1 > len2: return
            if len1 < 0 or len2 < 0: return
            if len1 == 0 and len2 == 0:
                out.append(''.join(path))
                return
            
            helper(len1 - 1, len2, path + ['('])
            helper(len1, len2 - 1, path + [')'])
        
        out = []
        helper(n, n, [])
        return out
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s, dic_t = {}, {} 
        
        for c1, c2 in zip(s, t):
            if (c1 not in dic_s) and (c2 not in dic_t):
                dic_s[c1] = c2
                dic_t[c2] = c1
            elif dic_s.get(c1) != c2 or dic_t.get(c2) != c1:
                return False
            
        return True
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:        
        stack = []
        out = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    out[i] = ''
                    continue
                stack.pop() 
        for i in stack:
            out[i] = ''
        return ''.join(out)
                    
                    
                
        
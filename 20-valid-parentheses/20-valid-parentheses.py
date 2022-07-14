class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        slist = dict({
            '(' : ')', 
            '[' : ']',
            '{' : '}'
        })
        
        for c in s:
            if c in slist.keys():
                stack.append(c)
            elif stack:
                last = stack.pop()
                if slist[last] != c:
                    return False
            else:
                return False
        return not stack
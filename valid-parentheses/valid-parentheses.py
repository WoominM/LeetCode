class Solution:
    def isValid(self, s: str) -> bool:
        lens = len(s)
        if lens%2 != 0 : return False
        # flag = True
        # while flag:
        #     if len(s) == lens:
        #         lens1 = lens
        #     s = s.replace('()','')
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        #     lens2 = len(s)
        #     if lens2 == lens1:
        #         flag = False
        #     else:
        #         lens1 = lens2
        #         if lens1 in [0, lens]:
        #             flag = False
        # return lens1 == 0

        dic = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for si in s:
            if si in dic:
                stack.append(si)
            elif stack and si == dic[stack[-1]]:
                stack.pop()
            else:
                return False
        return False if stack else True
                    
                    
        
                
        
                
        
        
                
                    
                    
                
                
        
        
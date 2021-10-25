class Solution:
    def isValid(self, s: str) -> bool:
        lens = len(s)
        flag = True
        while flag:
            if len(s) == lens:
                lens1 = lens
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
            lens2 = len(s)
            if lens2 == lens1:
                flag = False
            else:
                lens1 = lens2
                if lens1 in [0, lens]:
                    flag = False
        return lens1 == 0
                
        
        
                
                    
                    
                
                
        
        
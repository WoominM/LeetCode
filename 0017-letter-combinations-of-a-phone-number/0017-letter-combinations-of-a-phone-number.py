class Solution:
    def letterCombinations(self, digits: str) -> List[str]:     
        dic = {"2": "abc", "3": "def", "4":"ghi", 
               "5": "jkl", "6": "mno", "7": "pqrs", 
               "8": "tuv", "9": "wxyz"}
        
        if len(digits) == 0:
            return []
        
#         out = []
#         def helper(i, subc):
#             if i == len(digits):
#                 out.append(subc)
#                 return
            
#             for digit in dic[digits[i]]:
#                 helper(i + 1, subc + digit)
        
#         helper(0, '')
#         return out
    
        out = ['']
        for digit in digits:
            out = [item + c for item in out for c in dic[digit]]
        return out
    
    
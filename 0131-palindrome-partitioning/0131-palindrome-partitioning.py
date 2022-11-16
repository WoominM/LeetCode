class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def helper(string, path):
            if not string:
                out.append(path)
                return
            
            for i in range(len(string)):
                substring = string[:i+1]
                if isPal(substring):
                    helper(string[i+1:], path + [substring])
        
        out = []
        helper(s, [])
        return out
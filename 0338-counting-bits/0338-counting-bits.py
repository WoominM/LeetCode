class Solution:
    def countBits(self, n: int) -> List[int]:        
        # def convert(value, n):
        #     if value == 0:
        #         return str(value)
        #     temp = ''
        #     while value > 0:
        #         value, rem = divmod(value, n)
        #         temp += str(rem)
        #     return temp[::-1]
        
        def convert(value, n):
            if value == 0:
                return value
            temp = 0
            while value > 0:
                value, rem = divmod(value, n)
                temp += rem
            return temp
        
        out = [convert(i, 2) for i in range(n + 1)]
        return out
            
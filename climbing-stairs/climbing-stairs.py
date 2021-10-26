
class Solution:
    def factorial(self, n):
        result=1
        for i in range(2,n+1):
            result=result*i
        return result
    
    def combination(self, n, m):
        return self.factorial(n)//(self.factorial(n-m)*self.factorial(m))
    
    def climbStairs(self, n: int) -> int:
        max2step = n // 2
        
        ways = 1
        for num2step in range(1, max2step+1):
            num1 = n - 2*num2step
            ways += self.combination(num1+num2step, num1)
        return ways            

        
        # 11 / (11)
        # 111 / (11)1 / 1(11)         
        # 1111 / (11)11 / 1(11)1 / 11(11) / (11)(11)     
        # 11111 / (11)111 / 1(11)11 / 11(11)1 / 111(11) / (11)(11)1 / (11)1(11) / 1(11)(11)
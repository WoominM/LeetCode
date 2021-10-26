class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums = [8,-19,5,-4,20]
        # sub = []
        # flag = 0
        # lensub = 0
        # for i,num in enumerate(nums):
        #     if sub:
        #         sub.append(num)
        #         sums = sum(sub)
        #         if num > 0:     
        #             if flag == 0 and sum(sub[:-1]) <= 0 and num > maxsum:
        #                 sub = [num]
        #                 maxsum = num
        #                 lensub = 1
        #                 flag = 1
        #             elif sums > maxsum:
        #                 lensub += 1 if flag == 1 else (len(sub)-lensub)
        #                 maxsum = sums      
        #                 flag = 1
        #         else:
        #             sums_ = sum(sub[:-1])
        #             if flag == 0 and max(maxsum, sums_) < num:
        #                 sub = [num]
        #                 maxsum = num
        #                 lensub = 1
        #             flag = 0           
        #     else:
        #         sub.append(num)
        #         maxsum = num
        #         lensub += 1
        #         flag = 1 if num > 0 else 0
        #     print(sub, maxsum, lensub)
        # return sum(sub[:lensub])
        
        
        dp = [num for num in nums]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            
        return max(dp)
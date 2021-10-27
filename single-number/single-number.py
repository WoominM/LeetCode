class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     num = nums[0]
        #     nums.pop(nums.index(num))
        #     if num not in nums:
        #         return num
        #     else:
        #         nums.pop(nums.index(num))
        
        dic = {}
        for i,num in enumerate(nums):
            if num in dic.keys():
                del dic[num]
            else:
                dic[num] = 1
        return list(dic)[0]
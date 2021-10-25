class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i,num1 in enumerate(nums):
        #     num2 = target - num1
        #     start = i + 1            
        #     num2s = nums[start:]
        #     if num2 in num2s:
        #         return[i,start+num2s.index(num2)]      
        
        dic = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 not in dic:
                dic[num1] = i
            else:
                return [dic[num2], i]
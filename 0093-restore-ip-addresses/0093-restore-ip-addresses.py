class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def helper(nums, path):
            # if len(path) > 8:
            #     return
            if not nums:
                if len(path) == 8:
                    out.append(''.join(path[:-1]))
                return
            
            helper(nums[1:], path + [nums[:1], '.'])
            if 10 <= int(nums[:2]):
                helper(nums[2:], path + [nums[:2], '.'])
            if 100 <= int(nums[:3]) <= 255:
                helper(nums[3:], path + [nums[:3], '.'])
        
        out = []
        helper(s, [])
        return out
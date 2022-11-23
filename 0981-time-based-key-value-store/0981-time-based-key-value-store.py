class TimeMap:

    def __init__(self):
        self.hdic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hdic[key] += [[value, timestamp]]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hdic:
            return ''
        
        nums = self.hdic[key]
        target = timestamp
        
        left, right = 0, len(nums)
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot][1] == target:
                return nums[pivot][0]
            if nums[pivot][1] < target:
                left = pivot + 1
            elif nums[pivot][1] > target:
                right = pivot
        return '' if right == 0 else nums[right-1][0]

    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
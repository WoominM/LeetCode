class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for i in range(len(intervals)):
            # print(intervals[i], newInterval, left, right)
            if intervals[i][1] < newInterval[0]:
                left += intervals[i],
            elif intervals[i][0] > newInterval[1]:
                right += intervals[i],
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        return left + [newInterval] + right
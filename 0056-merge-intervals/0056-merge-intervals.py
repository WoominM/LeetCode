class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > prev[1]:
                out.append(prev)
                prev = intervals[i]
            else:
                prev[1] = max(prev[1], intervals[i][1])
            
        return out + [prev]
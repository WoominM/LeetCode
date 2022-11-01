class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        output = [intervals[0]]
        lastidx = 0
        for itv in intervals[1:]:
            if itv[0] <= output[lastidx][1]:
                output[lastidx][0] = min(itv[0], output[lastidx][0])
                output[lastidx][1] = max(itv[1], output[lastidx][1])
            else:
                output.append(itv)
                lastidx += 1
        return output
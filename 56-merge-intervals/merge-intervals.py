class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        merged = []
            
        intervals.sort()

        merged.append(intervals[0])
        for i in range(1, n):
            last_merged = merged[-1]
            
            if last_merged[1] >= intervals[i][0]:  
                last_merged[1] = max(last_merged[1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged
        
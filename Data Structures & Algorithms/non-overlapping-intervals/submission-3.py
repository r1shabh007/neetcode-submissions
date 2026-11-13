class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        last = intervals[0][0]
        for interval in intervals:
            if interval[0] < last:
                res += 1
                last = min(last, interval[1])
            else:
                last = interval[1]
        return res
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        intervals.sort()
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                lower, higher = intervals.pop(i)
                intervals[i - 1] = [min(intervals[i - 1][0], lower), max(intervals[i - 1][1], higher)]
                continue
            i += 1
        return intervals
        
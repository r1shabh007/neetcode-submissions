"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import bisect
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timings = []
        rooms = 0
        res = 0
        for interval in intervals:
            timings.append((interval.start, 1))
            timings.append((interval.end, -1))
        timings.sort()
        i = 0
        
        def updateRooms():
            nonlocal i
            nonlocal rooms
            time, status = timings[i]
            if status == 1:
                rooms += 1
            else:
                rooms -= 1
            i += 1

        while i < len(timings):
            updateRooms()
            while i < len(timings) and timings[i][0] == timings[i - 1][0]:
                updateRooms()
            res = max(res, rooms)
        return res



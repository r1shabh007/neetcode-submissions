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
        for interval in intervals:
            bisect.insort(timings, [interval.start, interval.end])
        active = []
        max_rooms = 0
        for start, end in timings:
            i = 0
            while i < len(active) and active[i] <= start:
                i += 1
            if i > 0:
                active = active[i:]
            bisect.insort(active, end)
            max_rooms = max(max_rooms, len(active))
        return max_rooms
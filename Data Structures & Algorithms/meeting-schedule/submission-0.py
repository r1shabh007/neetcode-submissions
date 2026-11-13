"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import bisect
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = []
        for interval in intervals:
            bisect.insort(meetings, [interval.start, interval.end])
        last = -math.inf
        for start, end in meetings:
            if start < last:
                return False
            last = end
        return True

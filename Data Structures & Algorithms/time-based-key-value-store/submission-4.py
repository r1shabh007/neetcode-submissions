import bisect
class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""
        values = self.time_map[key]
        l, r = 0, len(values)
        while l < r:
            mid = l + (r - l) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                l = mid
            else:
                r = mid
            if l + 1 == r:
                return values[l][1]

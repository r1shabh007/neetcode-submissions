class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # add num to small heap
        heapq.heappush(self.small, -1 * num)

        #if num added is too big add it to large heap
        if self.small and self.large and -(self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -(heapq.heappop(self.small)))

        #if small heap too big migrate max to large heap
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -(heapq.heappop(self.small)))

        #if large heap too big migrate min to small heap
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -(heapq.heappop(self.large)))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -(self.small[0])
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] - (self.small[0])) / 2
        
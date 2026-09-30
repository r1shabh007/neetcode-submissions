class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for number, frequency in count.items():
            freq[frequency].append(number)
        
        for i in range(len(nums), -1, -1):
            res.extend(freq[i])
            if k == len(res):
                return res
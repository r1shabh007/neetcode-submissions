class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        
        # create number:frequency pairings
        for i in nums:
            count[i] = count.get(i, 0) + 1

        # add those pairings into buckets
        for i in count.keys():
            freq[count[i]].append(i)

        # look for top k elements in buckets
        c = len(freq) - 1
        while len(res) < k:
            if freq[c] != 0:
                res.extend(freq[c])
            c -= 1
        return res
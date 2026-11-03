class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return 0
        b, s = prices[0], prices[0]
        for i in prices:
            if i < b:
                b, s = i, i
            if i > s:
                s = i
            res = max(res, s - b)
        return res


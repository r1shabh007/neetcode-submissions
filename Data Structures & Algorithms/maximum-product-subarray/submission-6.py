class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn, minn = 1, 1
        res = nums[0]
        for n in nums:
            tmpMax = maxn * n
            maxn = max(tmpMax, minn * n, n)
            minn = min(tmpMax, minn * n, n)
            res = max(res, maxn)
        return res
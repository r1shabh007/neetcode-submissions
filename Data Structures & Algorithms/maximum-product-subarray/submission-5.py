class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn, minn = 1, 1
        res = nums[0]
        for n in nums:
            iterlist = [maxn * n, minn * n, n]
            maxn = max(iterlist)
            minn = min(iterlist)
            res = max(res, maxn)
        return res
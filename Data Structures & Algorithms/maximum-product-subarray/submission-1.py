class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn, minn = 0, 0
        res = nums[0]
        for n in nums:
            if maxn == 0:
                maxn, minn = n, n
            else:
                iterlist = [maxn * n, minn * n, n]
                maxn = max(iterlist)
                minn = min(iterlist)
            res = max(res, maxn)
        return res
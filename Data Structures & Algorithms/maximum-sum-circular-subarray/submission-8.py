class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxn, minn = nums[0], nums[0]
        curMax = -float('inf')
        curMin = float('inf')
        for i in nums:
            total += i
            curMax = max(i, i + curMax)
            curMin = min(i, i + curMin)
            print(curMax, curMin)
            maxn = max(maxn, curMax)
            minn = min(minn, curMin)
        print(total)
        return max(total - minn, maxn) if total != minn else maxn
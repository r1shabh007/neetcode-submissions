class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        #print(dp)
        for i in range(len(nums) - 1, -1, -1):
            comparison = [1]
            for i2 in range(i + 1, len(dp) - 1):
                if nums[i] < nums[i2]:
                    comparison.append(dp[i2] + 1)
            #print(comparison)
            dp[i] = max(comparison)
        return max(dp)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_sum = current_sum = nums[0]
        while r < len(nums) - 1:
            r += 1
            if current_sum < 1:
                l = r
                current_sum = nums[r]
            else:
                current_sum += nums[r]
            max_sum = max(max_sum, current_sum)
        return max_sum

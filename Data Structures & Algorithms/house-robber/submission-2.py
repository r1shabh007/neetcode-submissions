class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            num1 = nums[0]
        if len(nums) == 1:
            return num1
        else:
            num2 = max(num1, nums[1])
        for i in range(2, len(nums)):
            res = max(num2, num1 + nums[i])
            num1 = num2
            num2 = res
        return num2
            
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i in range(0, len(nums) - 1):
            reach = nums[i] + i
            max_i = max(max_i, reach)
            if max_i <= i:
                return False
        return True
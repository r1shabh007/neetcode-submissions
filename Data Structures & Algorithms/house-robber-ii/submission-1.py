class Solution:
    def rob(self, nums: List[int]) -> int:
        def linearRob(nums: List[int]) -> int:
            n1, n2 = 0, 0
            for i in nums:
                val = max(i + n1, n2)
                n1 = n2
                n2 = val
            return n2
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(linearRob(nums[1:]), linearRob(nums[:-1]))
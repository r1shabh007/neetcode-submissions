class Solution:
    def rob(self, nums: List[int]) -> int:
        num1, num2 = 0, 0
        for n in nums:
            temp = max(n + num1, num2)
            num1 = num2
            num2 = temp
        return num2
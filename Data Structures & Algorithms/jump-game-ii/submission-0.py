class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            max_n = 0
            for i in range(l, r + 1):
                max_n = max(max_n, nums[i] + i)
            l = r + 1
            r = max_n
            res += 1
        return res

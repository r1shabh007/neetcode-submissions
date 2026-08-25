class Solution:
    def findMin(self, nums: List[int]) -> int:
        # want frame to shorten until left most digit is smallest
        # so the unordered side needs to progress leftmost side towards right, and the ordered side can just shorten
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
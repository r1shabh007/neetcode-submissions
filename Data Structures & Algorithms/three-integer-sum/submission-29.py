class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #left pointer progresses right
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            while l < r:
                target = nums[l] + nums[r] + n
                if target == 0:
                    minires = [n, nums[l], nums[r]]
                    if minires not in res:
                        res.append(minires)
                if target < 0:
                    l += 1
                else:
                    r -= 1
        return res

        #twosum on the remaining numbers
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first find the min number:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 # floor division
            if nums[m] < nums[r]: # if right frame is sorted, remove that frame
                r = m
            else: # otherwise the right frame has the min, and we need to shorten it
                l = m + 1
        # print("middle: ", nums[l], "index: ", l)
        m = l
        l, r = 0, len(nums) - 1
        while l < r:
            # print("l: ", l, "m: ", m, "r: ", r)
            if target >= nums[m] and target <= nums[r]: # if right frame contains val, remove left frame
                l = m
            else: #otherwise left frame contains val and progress frame left
                r = m - 1
            m =  -((l + r) // -2) #ceiling division
        return r if nums[r] == target else -1

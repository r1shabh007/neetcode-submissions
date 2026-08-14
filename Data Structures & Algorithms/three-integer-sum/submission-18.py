class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort list
        nums.sort()
        NUMLEN = len(nums)
        res = set()

        # handshake iteration to skip duplicates
        for i1, n1 in enumerate(nums):
        #l r pointers moving towards each other until they cross
            if n1 > 0:
                break

            if i1 > 0 and n1 == nums[i1 - 1]:
                continue

            l = i1 + 1 
            r = NUMLEN - 1

            while l < r:
                if n1 + nums[l] + nums[r] == 0 and l != r:
                    res.add(tuple([n1, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                    continue
                    # pairs added to list
                if n1 + nums[l] + nums[r] < 0:
                    l += 1
                    continue
                if n1 + nums[l] + nums[r] > 0:
                    r -= 1
                    continue
        return list(res)        

        
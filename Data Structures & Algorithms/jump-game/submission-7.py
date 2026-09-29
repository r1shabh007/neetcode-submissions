class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = set()
        i = 0
        while i < len(nums) - 1:
            seen.add(i)
            max_next_i = (0, i)
            for possible_jump in range(0, nums[i] + 1):
                n = i + possible_jump #checking the range for this hypothetical
                if n > len(nums) - 1:
                    return True
                next_i = n + nums[n] #range
                if next_i >= max_next_i[0]:
                    max_next_i = (next_i, n)
            i = max_next_i[1]
            print(i)
            if i in seen:
                return False
        return True
        
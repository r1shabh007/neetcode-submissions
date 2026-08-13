class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        LENGTH = len(nums)
        numbers = {}
        res = set()
        for i1, n1 in enumerate(nums):
            for i2, n2 in list(enumerate(nums))[i1+1:LENGTH]:
                diff = 0 - (n1 + n2)
                if n1 not in numbers:
                    numbers[n1] = i1
                if diff in numbers and i1 != numbers[diff] and i2 != numbers[diff]:
                    answer = [n1, n2, diff]
                    answer.sort()
                    res.add(tuple(answer))
        return list(res)
                     
                
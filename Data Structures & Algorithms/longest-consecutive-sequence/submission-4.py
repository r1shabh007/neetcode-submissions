class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # go through list
        # if number is smaller than anything prior
        list_lengths = {0}
        numset = set(nums)
        for x in numset:
            y = x
            if (x - 1) not in numset:
                while y in numset:
                    y += 1
            list_lengths.add(y - x)
        return(max(list_lengths))
        
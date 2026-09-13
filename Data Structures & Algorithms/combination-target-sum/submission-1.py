class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total):
            if i > len(nums) - 1:
                return
            if sum(total) == target:
                res.append(total.copy())
                return
            if sum(total) > target:
                return
            total.append(nums[i])
            dfs(i, total)
            total.pop()
            dfs(i + 1, total)
            return

        dfs(0, [])
        return res
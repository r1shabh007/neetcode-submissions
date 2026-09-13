class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, total):
            if i > len(nums) - 1:
                return
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            total += nums[i]
            path.append(nums[i])
            dfs(i, total)
            path.pop()
            total -= nums[i]
            dfs(i + 1, total)
            return

        dfs(0, 0)
        return res
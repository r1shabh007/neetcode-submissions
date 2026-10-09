class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        res = 0
        if n == 0 or n == 1:
            return 1
        for i in range(n - 1):
            res = a + b
            b = a
            a = res
        return res
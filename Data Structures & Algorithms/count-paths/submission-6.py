class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        print(dp)
        #bfs
        q = deque([(0,0)])
        seen = set((0,0))
        while q:
            a, b = q.popleft()
            if a - 1 >= 0:
                dp[a][b] += dp[a - 1][b]
            if b - 1 >= 0:
                dp[a][b] += dp[a][b - 1]
            possible_next_list = [(a, b + 1), (a + 1, b)]
            for possible_next in possible_next_list:
                if possible_next[0] < m and possible_next[1] < n and possible_next not in seen:
                    q.append(possible_next)
                    seen.add(possible_next)
        print(dp)
        return dp[m - 1][n - 1]
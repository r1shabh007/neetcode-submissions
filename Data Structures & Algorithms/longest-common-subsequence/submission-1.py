class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for i in range(len(text1))]
        res = 0
        #bfs
        q = deque([(0, 0)])
        seen = {(0, 0)}
        while q:
            t1, t2 = q.popleft()
            if text1[t1] == text2[t2]:
                dp[t1][t2] += 1
                if t1 + 1 < len(text1) and t2 + 1 < len(text2) and (t1 + 1, t2 + 1) not in seen:
                    q.append((t1 + 1, t2 + 1))
                    dp[t1 + 1][t2 + 1] = dp[t1][t2]
                    seen.add((t1 + 1, t2 + 1))
            else:
                next_possibles = [(t1, t2 + 1), (t1 + 1, t2)]
                for next_check in next_possibles:
                    if next_check[0] < len(text1) and next_check[1] < len(text2) and next_check not in seen:
                        q.append(next_check)
                        dp[next_check[0]][next_check[1]] = dp[t1][t2]
                        seen.add(next_check)
            res = max(res, dp[t1][t2])
        return res
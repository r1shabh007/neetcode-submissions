class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(i, j):
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                nxt = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for a, b in nxt:
                    a += r
                    b += c
                    if ((a, b) not in seen and
                        a >= 0 and a < len(grid) and
                        b >= 0 and b < len(grid[0]) and
                        grid[a][b] == "1"):
                        q.append((a, b))
                        seen.add((a, b))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    seen.add((i, j))
                    islands += 1
        return islands
        
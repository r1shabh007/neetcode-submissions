class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(i, j):
            q = deque([(i, j)])
            seen = {(i, j)}
            atl, pac = False, False
            while q:
                a, b = q.popleft()
                neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for pairs in neigh:
                    r, c = a + pairs[0], b + pairs[1]
                    if (r, c) not in seen:
                        if r < 0 or c < 0:
                            pac = True
                        elif r > len(heights) - 1 or c > len(heights[0]) - 1:
                            atl = True
                        elif heights[r][c] <= heights[a][b]:
                            seen.add((r, c))
                            q.append((r, c))
                    if atl and pac:
                        return True
        
        if not heights:
            return None
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs(i, j):
                    res.append([i, j])
        return res

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            seen = set(starts)
            q = deque(starts)
            while q:
                a, b = q.popleft()
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    r, c = a + dr, b + dc
                    if (0 <= r < rows and 0 <= c < cols
                            and (r, c) not in seen
                            and heights[r][c] >= heights[a][b]):
                        seen.add((r, c))
                        q.append((r, c))
            return seen

        pac = [(0, j) for j in range(cols)] + [(i, 0) for i in range(1, rows)]
        atl = [(rows - 1, j) for j in range(cols)] + [(i, cols - 1) for i in range(rows - 1)]

        return [list(cell) for cell in bfs(pac) & bfs(atl)]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        c = len(heights[0])
        r = len(heights)
        
        pac = [[None] * c for i in range(r)]
        pac[0] = [True] * c
        for i in range(r):
            pac[i][0] = True

        atl = [[None] * c for i in range(r)]
        atl[r - 1] = [True] * c
        for i in range(r):
            atl[i][c - 1] = True

        def bfs_pac(r1, c1) -> bool:
            q = deque([(r1, c1)])
            seen = {(r1, c1)}
            while q:
                r1, c1 = q.popleft()
                next_nodes = [(r1 - 1, c1),(r1, c1 - 1),(r1 + 1, c1),(r1, c1 + 1)]
                if pac[r1][c1] != None:
                    if pac[r1][c1]:
                        return True
                    else:
                        continue
                for r2, c2 in next_nodes:
                    if r2 < r and c2 < c and (r2, c2) not in seen and heights[r2][c2] <= heights[r1][c1]:
                        q.append((r2, c2))
                        seen.add((r2, c2))
            return False
        
        def bfs_atl(r1, c1) -> bool:
            q = deque([(r1, c1)])
            seen = {(r1, c1)}
            while q:
                r1, c1 = q.popleft()
                next_nodes = [(r1 - 1, c1),(r1, c1 - 1),(r1 + 1, c1),(r1, c1 + 1)]
                if atl[r1][c1] != None:
                    if atl[r1][c1]:
                        return True
                    else:
                        continue
                for r2, c2 in next_nodes:
                    if r2 >= 0 and c2 >= 0 and (r2, c2) not in seen and heights[r2][c2] <= heights[r1][c1]:
                        q.append((r2, c2))
                        seen.add((r2, c2))
            return False
        
        
        for i in range(r):
            for j in range(c):
                if bfs_pac(i,j):
                    pac[i][j] = True
                else:
                    pac[i][j] = False
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):                
                if bfs_atl(i,j):
                    atl[i][j] = True
                else:
                    atl[i][j] = False
        
        res = []
        for i in range(r):
            for j in range(c):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])
        return(res)

                        
                        





        
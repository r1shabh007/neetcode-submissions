from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # want to traverse nodes and record which ones are visited
        # want to see how many traversals were needed

        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()
        res = 0

        def bfs(node):
            q = deque([[node, -1]])
            visited.add(node)
            while q:
                curr_node, prev_node = q.popleft()
                for i in adj_list[curr_node]:
                    if i != prev_node and i not in visited:
                        q.append([i, curr_node])
                        visited.add(i)
        
        for i in range(n):
            if not i in visited:
                bfs(i)
                res += 1
        return res
        
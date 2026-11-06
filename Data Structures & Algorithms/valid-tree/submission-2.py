class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # as long as no cycles a tree can form
        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        print(adj_list)
        checked_nums = set()
        
        def dfs(node, seen, last_node):
            # base case 1
            if node in checked_nums:
                return True

            # base case 2
            if node in seen:
                return False
            seen.add(node)

            for i in adj_list[node]:
                if i != last_node and not dfs(i, seen, node):
                    return False
            
            seen.remove(node)
            checked_nums.add(node)
            return True

        if not dfs(0, set(), -1) or len(checked_nums) != n:
            return False
        return True

        
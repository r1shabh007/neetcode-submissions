"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}

        def dfs(node):
            #base case: return the copy
            if node in copies:
                return copies[node]

            #if no copy then make it
            new = Node()
            new.val = node.val
            copies[node] = new
            for neigh in node.neighbors:
                new.neighbors.append(dfs(neigh))
            return new
        
        return dfs(node) if node else None
        
        
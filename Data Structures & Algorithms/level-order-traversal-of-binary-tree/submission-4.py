# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #smarter BFS
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            row = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    row.append(node.val)
                    q.extend([node.left, node.right])
            if row:
                res.append(row)
        return res


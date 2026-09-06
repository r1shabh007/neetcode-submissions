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
            Qlen = len(q)
            for i in range(Qlen):
                node = q.popleft()
                if node:
                    row.append(node.val)
                    q.extend([node.left, node.right])
            if row:
                res.append(row)
        return res


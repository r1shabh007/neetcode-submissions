# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)

            maxLeft = max(0, maxLeft)
            maxRight = max(0, maxRight)
            res = max(res, root.val + maxLeft + maxRight)

            return root.val + max(maxLeft, maxRight)
        
        dfs(root)
        return res
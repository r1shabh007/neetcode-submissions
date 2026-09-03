# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = [root]

        while tree:
            node = tree.pop()
            if node:
                if node.val == subRoot.val and self.checkIdentical(node, subRoot):
                    return True
                tree.extend([node.right, node.left])
        return False
             

    def checkIdentical(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        treep = [p]
        treeq = [q]

        while treep or treeq:
            nodep, nodeq = treep.pop(), treeq.pop()
            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False
            treep.extend([nodep.right, nodep.left])
            treeq.extend([nodeq.right, nodeq.left])
        return True

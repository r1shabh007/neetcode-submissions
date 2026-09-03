# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #use array stack to represent tree. compare the pops
        tree1 = [p]
        tree2 = [q]
        while tree1 or tree2:
            node1, node2 = tree1.pop(), tree2.pop()
            if not node1 and not node2:
                continue
            
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            tree1.extend([node1.right, node1.left])
            tree2.extend([node2.right, node2.left])
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = ListNode(0, head)
        turn = 0
        while head:
            if head == pointer:
                return True
            head = head.next
            pointer = pointer.next if (turn % 2) else pointer
            turn += 1
        return False
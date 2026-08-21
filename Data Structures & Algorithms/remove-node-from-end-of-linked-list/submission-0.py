# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next
        num = counter - n
        print("num: ", num, "counter: ", counter, "n: ", n)
        if num == 0:
            return head.next
        else:
            curr = head
            counter = 1
            while curr:
                nxt = curr.next
                if counter == num:
                    nxt = nxt.next
                    curr.next = nxt
                    counter += 2
                else:
                    counter += 1
                curr = nxt
            return head
            
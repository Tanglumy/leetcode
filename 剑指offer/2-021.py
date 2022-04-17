# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = []
        dummy = ListNode(0, head)
        x = dummy
        while x:
            stack.append(x)
            x = x.next
        for i in range(n):
            stack.pop()
        del_w = stack[-1]
        del_w.next = del_w.next.next
        return dummy.next

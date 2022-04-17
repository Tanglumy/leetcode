# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = head
        stack = []
        if not dummy:
            return None
        while dummy:
            stack.append(dummy)
            dummy = dummy.next
        n = len(stack)
        for i in range(n):
            stack[i].next = None
        for i in range(n-1, 0, -1):
            stack[i].next = stack[i-1]
            if i-1 == 0:
                stack[i-1] = None
        return stack[-1]

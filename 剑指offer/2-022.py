# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dummy = head
        stack = []
        while dummy:
            if dummy in stack:
                return dummy
            stack.append(dummy)
            dummy = dummy.next
        return None

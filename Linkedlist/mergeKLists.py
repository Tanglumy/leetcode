# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        stack = []
        for index, i in enumerate(lists):
            while i:
                stack.append(i)
                i = i.next
        stack = sorted(stack, key=lambda s: s.val)
        for i in stack:
            i.next = None
        for i in range(len(stack)-1):
            stack[i].next = stack[i+1]
        return stack[0] if stack else None

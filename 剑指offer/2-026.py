# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        dummy = head
        while dummy:
            stack.append(dummy)
            dummy = dummy.next
        l, r = 0, -1
        for i in stack:
            i.next = None
        print(stack)
        while l-r < len(stack):
            stack[l].next = stack[r]
            if stack[r] != stack[l+1]:
                stack[r].next = stack[l+1]
            print(stack[l])
            l += 1
            r -= 1
        return dummy

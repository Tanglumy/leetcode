# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        dummy = head
        while dummy:
            stack.append(dummy)
            dummy = dummy.next
        l, r = 0, -1
        while l-r <= len(stack):
            if stack[l].val == stack[r].val:
                l += 1
                r -= 1
            else:
                return False
        return True

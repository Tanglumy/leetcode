# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA = []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            if headB in stackA:
                return headB
            headB = headB.next
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2=[]
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        result = []
        while stack1 or stack2:
            temp1 = stack1.pop().val if stack1 else 0
            temp2 = stack2.pop().val if stack2 else 0
            print(temp1,temp2)
            result.append(temp1+temp2)
        # 处理进位
        for i in range(len(result)):
            if result[i]>=10 and i!=len(result)-1:
                result[i]-=10
                result[i+1]+=1
            elif result[i]>=10 and i==len(result)-1:
                result.append(1)
                result[i]-=10
        print(result)
        head = ListNode()
        dummy = head
        while result:
            head.val = result.pop()
            if result:
                head.next = ListNode()
            head = head.next
        return dummy
                
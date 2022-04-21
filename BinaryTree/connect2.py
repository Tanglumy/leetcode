"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ndeque = deque()
        ndeque.append(root)

        def search(root):

            while root:
                if not ndeque:
                    return
                for i in range(len(ndeque)-1):
                    ndeque[i].next = ndeque[i+1]
                    ndeque[-1].next = None
                for i in range(len(ndeque)):
                    x = ndeque.popleft()
                    if x.left:
                        ndeque.append(x.left)
                    if x.right:
                        ndeque.append(x.right)
        search(root)
        return root

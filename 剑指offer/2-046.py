# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        ndeque = deque()
        ndeque.append(root)
        while ndeque:
            n = len(ndeque)-1
            for i in range(n+1):
                x = ndeque.popleft()
                if i ==  n:
                    print(x.val)
                    res.append(x.val)
                if x.left:
                    ndeque.append(x.left)
                if x.right:
                    ndeque.append(x.right)

        return res


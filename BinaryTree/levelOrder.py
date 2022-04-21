# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ndeque = deque()
        ndeque.append(root)
        res = []
        while ndeque:
            res.append([])
            for i in range(len(ndeque)):
                x = ndeque.popleft()
                res[-1].append(x.val)
                if x.left:
                    ndeque.append(x.left)
                if x.right:
                    ndeque.append(x.right)

        return res

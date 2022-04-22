# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        ret = root.val
        while queue:
            for i in range(len(queue)):
                q = queue.popleft()
                if i == 0:
                    ret = q.val
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return ret

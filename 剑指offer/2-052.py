# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            stack.append(root)
            dfs(root.right)
        dfs(root)
        for i in range(len(stack)):
            stack[i].left = None
            stack[i].right = None
        for i in range(len(stack)-1):
            stack[i].right = stack[i+1]
        return stack[0]
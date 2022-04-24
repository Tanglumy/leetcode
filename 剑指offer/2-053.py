# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
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
            if stack[i] == p:
                return stack[i+1]
        return None

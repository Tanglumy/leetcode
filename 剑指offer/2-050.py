class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def DFS(root):
            if not root:
                return 0
            left_part = DFS(root.left)
            right_part = DFS(root.right)
            self.ans = max(self.ans, left_part + root.val + right_part)
            return max(0, root.val, root.val + left_part, root.val + right_part)

        self.ans = root.val
        DFS(root)
        return self.ans

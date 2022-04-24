class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root

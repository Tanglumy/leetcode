# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Definition for a binary tree node.
        res = []

        def porder(root):
            if not root:
                return
            porder(root.left)
            porder(root.right)
            res.append(root.val)
        porder(root)
        print(res)
        return res

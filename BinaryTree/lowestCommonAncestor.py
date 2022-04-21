# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:  # 左右子树都有结果，2节点分列两边，返回父root
            return root
        if not l and not r:  # 都没找到返回空
            return None
        return l if l else r  # 只有1个有结果，在同一子树上，返回即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode()
        x = preorder[0]
        root.val = x
        if x in inorder:
            key = inorder.index(x)
        else:
            return None
        root.left = self.buildTree(preorder[1: key + 1], inorder[0: key])
        root.right = self.buildTree(preorder[key+1:], inorder[(key+1):])
        return root

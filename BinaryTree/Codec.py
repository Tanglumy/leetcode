# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        queue_str = deque(data[1:-1].split(", "))
        print(queue_str)

        def str_to_node(node_str):
            if node_str == "" or node_str == "None":
                return None
            return TreeNode(int(node_str))

        def dfs_merge():
            if not queue_str:
                return None
            node_str = queue_str.popleft()

            node = str_to_node(node_str)
            if node:
                node.left = dfs_merge()
                node.right = dfs_merge()

            return node

        return dfs_merge()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

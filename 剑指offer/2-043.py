# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.ndeque = deque([])
        stack = deque([root])
        while stack:
            cur_node = stack.popleft()
            if not cur_node.left or not cur_node.right:
                self.ndeque.append(cur_node)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

    def insert(self, v: int) -> int:
        self.ndeque.append(TreeNode(v))
        if self.ndeque[0].left:
            self.ndeque[0].right = self.ndeque[-1]
            return self.ndeque.popleft().val
        else:
            self.ndeque[0].left = self.ndeque[-1]
            return self.ndeque[0].val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

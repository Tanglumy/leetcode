class Solution:
    def largestValues(self, root):
        ret, queue = [], deque()
        if root:
            queue.append(root)
        while queue:
            num = -float('inf')
            for i in range(len(queue)):
                q = queue.popleft()
                num = max(num, q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            ret.append(num)
        return ret

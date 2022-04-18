def largestRectangleArea(heights) -> int:
    '''
    剑指 Offer II 039. 直方图最大矩形面积
    '''
    stack = [(-1, -1)]
    H = heights+[0]
    ans = 0
    for i, h in enumerate(H):
        while stack[-1][1] > h:
            _, oh = stack.pop()
            s = (i-stack[-1][0]-1)*oh
            ans = max(ans, s)
        stack.append((i, h))
    return ans


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        M = matrix
        if not M:
            return 0
        m = len(M)
        n = len(M[0])
        dp = [0]*n
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if M[i][j] == '0' else dp[j]+1
            ans = max(ans, largestRectangleArea(dp))
        return ans

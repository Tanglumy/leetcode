class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for index, i in enumerate(temperatures):
            if not stack:
                stack.append(index)
            else:
                while temperatures[stack[-1]] < i:
                    x = stack.pop()
                    result[x] = index-x
                    if not stack:
                        break
                stack.append(index)
        return result
# 单调栈

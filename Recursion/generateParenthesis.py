class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n == 1:
            return ["()"]
        else:
            ret = []
            for i in self.generateParenthesis(n-1):
                ret.append("()"+i)
                for j in range(1, len(i)):
                    ret.append(i[0:j]+"()"+i[j:])
            return list(set(ret))

class Solution:
    def countSubstrings(self, s: str) -> int:

        n, ans = len(s), 0
        substr_map = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:  # 单独字符必定是回文串
                    substr_map[i][j] = 1
                elif i == j-1:  # 相邻字符若相同则是回文串
                    substr_map[i][j] = 1 if s[i] == s[j] else 0
                else:  # 其余情况，只与两端字符相等，且中间是回文串有关
                    substr_map[i][j] = substr_map[i +
                                                  1][j-1] if s[i] == s[j] else 0
            ans += sum(substr_map[i])
        return ans

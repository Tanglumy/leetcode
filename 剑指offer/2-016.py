class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, len(occ))
        return ans

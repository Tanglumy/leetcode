class Solution:
    def minWindow(self, s: str, t: str) -> str:
        j, res = 0, ''
        t = Counter(t)
        c = Counter()
        for i in range(len(s)):
            if s[i] in t:
                c[s[i]] += 1
                while j <= i and not t-c:
                    if not res or len(res) > i-j+1:
                        res = s[j:i+1]
                    if s[j] in c:
                        c[s[j]] -= 1
                    j += 1
        return res

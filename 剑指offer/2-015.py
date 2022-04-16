class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_l = len(s)
        p_l = len(p)
        result = []
        y = collections.Counter(p)
        x = collections.Counter(s[:p_l])
        z = collections.Counter(None)
        if x == y:
            result.append(0)
        for i in range(1, s_l-p_l+1):
            x[s[i-1]] -= 1
            x[s[i+p_l-1]] += 1
            if x-y == z:
                result.append(i)
        return result

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if collections.Counter(s) == collections.Counter(t):
            return True
        return False

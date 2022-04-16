class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_l = len(s1)
        s2_l = len(s2)
        for i in range(s2_l):
            if collections.Counter(s2[i:i+s1_l]) == collections.Counter(s1):
                return True
        return False

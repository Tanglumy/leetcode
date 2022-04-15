class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def diff(words1, words2):
            goal1 = set(list(words1))
            goal2 = set(list(words2))
            goal3 = set(list(words1+words2))
            n = len(goal3)
            m = len(goal1)+len(goal2)
            if m == n:
                return True
            else:
                return False
            return True
        n = len(words)
        result = 0
        for i in range(0, n):
            for j in range(i, n):
                if diff(words[i], words[j]):
                    result = max(result, len(words[i])*len(words[j]))
        return result

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {j: i for i, j in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w1_len = words[i], len(words[i])
            w2, w2_len = words[i + 1], len(words[i + 1])
            for idx in range(max(w1_len, w2_len)):
                w1_idx = -1 if idx >= w1_len else dic[w1[idx]]
                w2_idx = -1 if idx >= w2_len else dic[w2[idx]]
                if w1_idx > w2_idx:
                    return False
                if w1_idx < w2_idx:
                    break
        return True
# 真心没看懂题目

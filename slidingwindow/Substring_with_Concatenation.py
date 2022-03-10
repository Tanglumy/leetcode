# link: https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        re = []
        re2 = {}
        for i in words:
            if i in re2:
                re2[i] += 1
            else:
                re2[i] = 1
        # print(re2)
        n = len(s)
        m = len(words[0])
        all_len = len(words) * m
        right, left = m, -1
        flag = 0
        for i in range(0, n - all_len + 1):
            re3 = re2.copy()
            left += 1
            right += 1
            leftr, rightr = left, right
            while leftr+1 <= n and s[leftr:rightr-1] in words:
                if re3[s[leftr:rightr-1]] >= 1:
                    re3[s[leftr:rightr-1]] -= 1
                    # re.append(s[leftr:rightr-1])
                    # print(s[leftr:rightr-1],re3[s[leftr:rightr-1]])
                else:
                    break
                if flag == 0:
                    temp = leftr
                    flag = 1
                    # print(temp)
                if all(i == 0 for i in re3.values()):
                    result.append(temp)
                rightr += m
                leftr += m
                # print(re2,re,result)
            flag = 0
        return result

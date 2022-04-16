class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        slen = len(s)
        i, j = 0, slen - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                s = s[i:j+1]
                break
        temp1 = s[:-1]
        temp2 = s[1:]
        if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
            return True
        return False

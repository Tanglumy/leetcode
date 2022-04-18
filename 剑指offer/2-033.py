class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        counters = []
        kv = {}
        for i in range(n):
            y = str(sorted(strs[i]))
            if y in kv:
                kv[y].append(strs[i])
            else:
                kv[y] = []
                kv[y].append(strs[i])
        return list(kv.values())

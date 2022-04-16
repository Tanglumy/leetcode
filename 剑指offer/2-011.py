class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        presum_map = {0: -1}
        presum, ans = 0, 0

        for i, num in enumerate(nums):
            if num == 1:
                presum += 1
            else:
                presum -= 1

            if presum in presum_map:
                ans = max(ans, i - presum_map[presum])
            else:
                presum_map[presum] = i

        return ans

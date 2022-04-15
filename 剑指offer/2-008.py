class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums.sort()
        n = len(nums)
        left, right = 0, 0
        result = n
        if sum(nums) < target:
            return 0
        while right != n:
            x = sum(nums[left:right+1])
            if x >= target:
                result = min(result, right-left+1)
                print(nums[left], nums[right])
                left += 1
            else:
                right += 1
        return result

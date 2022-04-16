class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_all = sum(nums)
        sum_temp = 0
        for i, num in enumerate(nums):
            if num == sum_all-2*sum_temp:
                return i
            sum_temp += num
        return -1

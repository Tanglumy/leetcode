class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(result, nums, target):
            left, right = 0, len(nums)-1
            while left != right:
                n = nums[left]+nums[right]
                if n == target:
                    t = [-target, nums[left], nums[right]]
                    if t not in result:
                        result.append(t)
                    right -= 1
                elif n > target:
                    right -= 1
                else:
                    left += 1
        nums.sort()
        result = []
        if len(nums) < 3:
            return []
        for i in range(len(nums)-1):
            target = -nums[i]
            y = nums[i+1:]
            twoSum(result, y, target)
        return result


# https://leetcode-cn.com/problems/1fGaJU/

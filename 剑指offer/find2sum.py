# ttps://leetcode-cn.com/problems/kLl5u1/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left != right:
            x = numbers[left]+numbers[right]
            if x == target:
                return [left, right]
            elif x > target:
                right -= 1
            else:
                left += 1

// https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums_increase = nums[:]
        nums_decrease = nums[:]
        nums_increase.sort()
        nums_decrease.sort(reverse=True)

        if nums == nums_increase:
            return True
        elif nums == nums_decrease:
            return True
        else:
            return False

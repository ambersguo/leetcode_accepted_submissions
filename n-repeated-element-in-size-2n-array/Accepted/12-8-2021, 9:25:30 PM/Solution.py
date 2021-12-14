// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        n = int(len(nums)/2)
        if nums[n-1] == nums[n]:
            return nums[n]
        else:
            if nums[n-2] == nums[n-1]:
                return nums[n-1]
            else:
                return nums[n]

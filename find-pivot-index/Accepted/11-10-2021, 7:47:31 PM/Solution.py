// https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(0,len(nums)):
            if right - left == nums[i]:
                return i        
            right -= nums[i]
            left += nums[i]
        return -1

// https://leetcode.com/problems/largest-perimeter-triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                peri = nums[i] + nums[i+1] + nums[i+2]
                return peri
            else:
                next
        return 0

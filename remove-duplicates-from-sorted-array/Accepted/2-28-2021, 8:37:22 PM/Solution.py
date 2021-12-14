// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            pre = nums[0]
            i = 1
            while i < len(nums):
                if nums[i] == pre:
                    pre = nums[i]
                    nums.pop(i)
                else:
                    pre = nums[i]
                    i += 1
            return len(nums)
        else:
            return 0

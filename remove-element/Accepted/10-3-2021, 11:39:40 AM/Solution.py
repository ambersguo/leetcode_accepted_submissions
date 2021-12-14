// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums:
            nums.sort()
            i = 0
            while i < len(nums):
                if nums[i] < val:
                    i += 1
                    next
                elif nums[i] == val:
                    nums.pop(i)
                else:
                    break
            return len(nums)
        else:
            return 0
        
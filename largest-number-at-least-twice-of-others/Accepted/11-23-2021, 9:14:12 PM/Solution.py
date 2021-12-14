// https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            nums_sorted = nums[:]
            nums_sorted = list(set(nums_sorted))
            nums_sorted.sort(reverse = True)
            first = nums_sorted[0]
            second = nums_sorted[1]
            if second != 0 and first/second < 2:
                return -1
            else:
                for i in range(len(nums)):
                    if nums[i] == first:
                        return i

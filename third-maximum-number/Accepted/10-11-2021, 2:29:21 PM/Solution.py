// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_uniq = list(set(nums))
        nums_uniq.sort(reverse=True)
        if len(nums_uniq) > 2:
            return nums_uniq[2]
        else:
            return nums_uniq[0]
  
// https://leetcode.com/problems/smallest-range-i

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = nums[0]
        high = nums[-1]
        diff = high - low
        check = diff - k*2
        if check > 0:
            return check
        else:
            return 0
       
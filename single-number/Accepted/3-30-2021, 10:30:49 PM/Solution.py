// https://leetcode.com/problems/single-number

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        return list(nums_count.keys())[list(nums_count.values()).index(1)]

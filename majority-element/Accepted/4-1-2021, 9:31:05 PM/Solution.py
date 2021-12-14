// https://leetcode.com/problems/majority-element

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_list = Counter(nums).most_common()
        return count_list[0][0]
        
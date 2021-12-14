// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        set1 = set(nums1)
        set2 = set(nums2)
        for n in set1:
            if n in set2:
                intersection.append(n)
        return intersection

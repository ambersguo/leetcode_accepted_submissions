// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for n in nums1:
            if n in nums2:
                intersection.append(n)
                nums2.remove(n)
        return intersection

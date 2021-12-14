// https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2dict = {}
        ans = []
        for i in range(len(nums2)):
            nums2dict[i] = nums2[i]
        for n in nums1:
            keys = [key for key, value in nums2dict.items() if value == n]
            check = 0
            for j in range(keys[0],len(nums2)):
                if nums2[j] > n:
                    ans.append(nums2[j])
                    check = 1
                    break
            if not check:
                ans.append(-1)
        return ans

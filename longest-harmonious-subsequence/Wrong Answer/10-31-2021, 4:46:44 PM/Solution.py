// https://leetcode.com/problems/longest-harmonious-subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        index2value = {}
        maxlist = []
        for i in range(len(nums)):
            index2value[i] = nums[i]
        nums2 = nums
        nums2.sort()
        nums_uniq = list(set(nums2))
        for i in range(len(nums_uniq)-1):
            if nums_uniq[i+1] - nums_uniq[i] == 1:
                indice = []
                for index, value in index2value.items():
                    if value == nums_uniq[i] or value == nums_uniq[i+1]:
                        indice.append(index)
                maxlist.append(len(indice))
        maxlist.sort()
        if maxlist:
            return maxlist[-1]
        else:
            return 0

// https://leetcode.com/problems/longest-harmonious-subsequence

from collections import defaultdict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        value2count = {}
        value2count = defaultdict(lambda:0,value2count)
        maxlist = []
        for n in nums:
            value2count[n] += 1
        nums2 = nums
        nums_uniq = [int(n) for n in set(nums2)]
        nums_uniq.sort()
        for i in range(len(nums_uniq)-1):
            if nums_uniq[i+1] - nums_uniq[i] == 1:
                maxlen = value2count[nums_uniq[i]] + value2count[nums_uniq[i+1]]
                maxlist.append(maxlen)
        maxlist.sort()
        if maxlist:
            return maxlist[-1]
        else:
            return 0

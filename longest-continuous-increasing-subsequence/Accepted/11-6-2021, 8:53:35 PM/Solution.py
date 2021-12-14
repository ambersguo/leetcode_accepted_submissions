// https://leetcode.com/problems/longest-continuous-increasing-subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        counts = []
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        counts.sort(reverse=True)
        return counts[0]

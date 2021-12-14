// https://leetcode.com/problems/array-partition-i

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 0
        for i in range(0,len(nums),2):
            total += min(nums[i], nums[i+1])
        return total

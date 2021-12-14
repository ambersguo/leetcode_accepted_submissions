// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num2index = {}
        miss = rep = ''
        for i in range(len(nums)):
            if nums[i] in num2index.keys():
                rep = nums[i]
                if miss:
                    return [rep,miss]
            else:
                num2index[nums[i]] = i

            if i+1 not in nums:
                miss = i+1
                if rep:
                    return [rep,miss]

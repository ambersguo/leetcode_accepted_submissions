// https://leetcode.com/problems/two-sum

import random
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            minus = target - nums[i]
            if minus in nums:
                index1 = i
                index2 = nums.index(minus)
                if index1 == index2:
                    i += 1
                else:
                    break
            else:
                i += 1
        return [index1, index2]
       
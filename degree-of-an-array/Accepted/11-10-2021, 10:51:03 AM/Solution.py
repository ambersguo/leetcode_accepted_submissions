// https://leetcode.com/problems/degree-of-an-array

from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num2indice = defaultdict(list)
        num2count = defaultdict(lambda:0)
        max_nums = []
        lengths = []
        for i in range(len(nums)):
            num2indice[nums[i]].append(i)
            num2count[nums[i]] += 1
        degree = max(num2count.values())
        for key, value in num2count.items():
            if value == degree:
                max_nums.append(key)
        for num in max_nums:
            num2indice[num].sort()
            length = num2indice[num][-1] - num2indice[num][0] + 1
            lengths.append(length)
        lengths.sort()
        return lengths[0]

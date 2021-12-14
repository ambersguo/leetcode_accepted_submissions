// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        for i in range(len(nums)-k+1):
            if i == 0:
                sum_max = sum(nums[:k])
                sum_last = sum_max
            else:
                sum_cur = sum_last - nums[i-1] + nums[i+k-1]
                if sum_cur > sum_max:
                    sum_max = sum_cur
                sum_last = sum_cur
        return sum_max/k

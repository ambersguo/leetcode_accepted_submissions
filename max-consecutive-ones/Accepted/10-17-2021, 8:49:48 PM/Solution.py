// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums_str = ''.join([str(n) for n in nums])
        nums_chunks = nums_str.split('0')
        nums_chunks.sort(reverse = True)
        max_len = len(nums_chunks[0])
        return max_len

// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = int((start+end)/2)
            if target in nums[start:mid+1]:
                end = mid
            elif target in nums[mid+1:end+1]:
                start = mid+1
            else:
                return -1
        return start

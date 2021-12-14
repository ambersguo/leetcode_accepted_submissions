// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        nums_len = len(nums)
        if nums_len > 1:
            while i < nums_len:
                if nums[i] == 0:
                    nums.pop(i)
                    count+=1
                    nums_len-=1
                else:
                    i+=1
            for i in range(count):
                nums.append(0)

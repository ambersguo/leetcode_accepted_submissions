// https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        obj = self.nums
        sum = 0
        for n in range(left, right+1):
            sum += obj[n]
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
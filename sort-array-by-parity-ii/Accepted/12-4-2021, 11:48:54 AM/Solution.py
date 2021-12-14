// https://leetcode.com/problems/sort-array-by-parity-ii

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums2 = []
        odds = []
        evens = []
        result = []
        
        for i in range(len(nums)):
            if i%2 == 0 and nums[i]%2 != 0:
                nums2.append('even')
                odds.append(nums[i])
            elif i%2 != 0 and nums[i]%2 == 0:
                nums2.append('odd')
                evens.append(nums[i])
            else:
                nums2.append(nums[i])
                
        for n in nums2:
            if n == 'even':
                result.append(evens.pop(0))
            elif n == 'odd':
                result.append(odds.pop(0))
            else:
                result.append(n)
        
        return result

// https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        result = []
        for n in nums:
            if n%2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        result = evens + odds
        return result

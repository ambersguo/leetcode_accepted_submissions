// https://leetcode.com/problems/arranging-coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        total = -1
        while n>=0:
            n = n - i
            total += 1
            i+= 1
        return total
   
// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for n in range(1,num+1):
            if num/n == n:
                return True
            else:
                if num/n < n:
                    break
        return False

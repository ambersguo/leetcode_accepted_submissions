// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:       
        n = int(x/2)
        if n:
            while x < n*n:
                n = int(n/2)
            while x > (n+1)*(n+1) or x == (n+1)*(n+1):
                n += 1
            return n
        else:
            return x
   
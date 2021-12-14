// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        fibs = [0,1]
        for i in range(2, n+1):
            x = fibs[i-1] + fibs[i-2]
            fibs.append(x)
        return fibs[n]

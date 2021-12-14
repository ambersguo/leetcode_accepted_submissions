// https://leetcode.com/problems/ugly-number

class Solution:
    def isUgly(self, n: int) -> bool:
        primes = [2,3,5]
        if n <= 0:
            return False
        while n > 1:
            for prime in primes:
                check = 0
                if n%prime == 0:
                    n = n/prime
                    print(n)
                    check = 1
                    break
            if not check:
                return False
        return True

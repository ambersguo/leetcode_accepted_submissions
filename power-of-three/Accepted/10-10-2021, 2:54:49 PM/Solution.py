// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            while n > 1:
                if n%3 == 0:
                    n = n/3
                    if n == 1:
                        return True
                else:
                    return False

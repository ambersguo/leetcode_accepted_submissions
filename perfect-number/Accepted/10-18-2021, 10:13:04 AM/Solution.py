// https://leetcode.com/problems/perfect-number

import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sqrt = int(math.sqrt(num))
        total = 1
        for n in range(2,sqrt+1):
            if num%n == 0:
                total = total + n + num/n
        if total == num:
            return True
        else:
            return False

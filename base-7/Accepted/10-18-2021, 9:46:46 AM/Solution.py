// https://leetcode.com/problems/base-7

class Solution:
    def convertToBase7(self, num: int) -> str:
        check = 0
        if num == 0:
            return '0'
        elif num < 0:
            num = -num
            check = 1
        digits = []
        while num:
            digits.append(int(num % 7))
            num //= 7
        digits_r = digits[::-1]
        digits_str = ''.join([str(d) for d in digits_r])
        if check:
            digits_str = '-' + digits_str
        return digits_str

// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = [str(digit) for digit in digits]
        number = int(''.join(digits_str))
        number += 1
        digits_new = [int(n) for n in str(number)]
        return digits_new
        
// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while len(str(num)) > 1:
            for n in list(str(num)):
                total += int(n)
            num = total
            total = 0
        return num

// https://leetcode.com/problems/binary-number-with-alternating-bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n_bin = str(format(n,'08b'))
        d_pre = '0'
        check1 = check2 = 0
        for d in n_bin:
            if d == '1':
                check1 = check2 = 1
                if d_pre != '0':
                    return False
            elif check1:
                check1 = 0
                if d == '1':
                    return False
            elif d == '0' and check2:
                return False
            d_pre = d
        return True

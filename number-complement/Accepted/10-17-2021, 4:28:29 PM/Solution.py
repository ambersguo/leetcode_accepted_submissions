// https://leetcode.com/problems/number-complement

class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = str(format(num,'b'))
        new_num_bin = ""
        for n in num_bin:
            if n == '1':
                new_num_bin = new_num_bin + '0'
            else:
                new_num_bin = new_num_bin + '1'
        new_num = int(new_num_bin,2)
        return new_num

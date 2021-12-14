// https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = str(format(x,'08b'))
        y_bin = str(format(y,'08b'))
        ham = 0
        diff= abs(len(x_bin)-len(y_bin))
        if diff:
            add_zero = '0'*diff
            if len(x_bin) > len(y_bin):
                y_bin = add_zero + y_bin
            else:
                x_bin = add_zero + x_bin 
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                ham+=1
        return ham

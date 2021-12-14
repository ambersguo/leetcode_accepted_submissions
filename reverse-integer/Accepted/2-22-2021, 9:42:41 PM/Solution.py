// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x_test = -x
            x_backward_list = list(str(x_test))[::-1]
            x_backward = int(''.join(x_backward_list))
            x_return = -x_backward
        else:
            x_test = x
            x_backward_list = list(str(x_test))[::-1]
            x_backward = int(''.join(x_backward_list))
            x_return = x_backward
        
        if x_return in range(-2**31, 2**31-1):
            return x_return
        else:
            return 0

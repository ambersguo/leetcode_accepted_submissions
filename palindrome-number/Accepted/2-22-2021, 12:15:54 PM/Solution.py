// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==abs(x):
            x_backward_list = list(str(x))[::-1]
            x_backward = int(''.join(x_backward_list))
            return x==x_backward
        else:
            return x==abs(x)
        
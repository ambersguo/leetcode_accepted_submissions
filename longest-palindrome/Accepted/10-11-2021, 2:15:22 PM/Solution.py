// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = 0
        check = 0
        while s:
            c = s[0]
            s = s.replace(c,'',1)
            if c in s:
                s = s.replace(c,'',1)
                n+=1
            else:
                check+=1
        if check:
            length = 2*n + 1
        else:
            length = 2*n
        return length

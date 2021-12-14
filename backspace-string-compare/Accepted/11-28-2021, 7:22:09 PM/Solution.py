// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2 = t2 = ''
        for c in s:
            if c == '#':
                s2 = s2[:-1]
            else:
                s2 += c
        for c in t:
            if c == '#':
                t2 = t2[:-1]
            else:
                t2 += c

        if s2 == t2:
            return True
        else:
            return False

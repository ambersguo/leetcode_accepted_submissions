// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        s_r = s[::-1]
        while s_r:
            first = s_r[0]
            s_r = s_r[1:]
            if first in brackets.keys():
                first_match = brackets.get(first)
                if first_match in s_r:
                    s_r = s_r.replace(first_match,'',1)
                    next
                else:
                    return False
            else:
                return False
        return True

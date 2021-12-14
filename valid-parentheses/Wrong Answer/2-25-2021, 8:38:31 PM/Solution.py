// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        s_split = set([s[i:i+2] for i in range(0, len(s), 2)])
        for brackets in s_split:
            if brackets == '()' or brackets =='{}' or brackets == '[]':
                next
            else:
                return False
        return True

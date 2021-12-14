// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 0:
            first_half  = s[0:len(s)//2]
            second_half = s[len(s)//2:]
            second_half_r = second_half[::-1]
            count = 0
            for m in first_half:
                for n in second_half_r:
                    if (m == '(' and n == ')') or (m == '{' and n == '}') or (m == '[' and n == ']'):
                        count+=1
            if count == len(first_half):
                return True
            else:
                s_split = set([s[i:i+2] for i in range(0, len(s), 2)])
                for brackets in s_split:
                    if brackets == '()' or brackets =='{}' or brackets == '[]':
                        next
                    else:
                        return False
                return True
        else:
            return False

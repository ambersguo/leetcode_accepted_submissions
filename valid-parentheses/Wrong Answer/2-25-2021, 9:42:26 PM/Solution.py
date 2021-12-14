// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 0:
            first = s[0:len(s)//2]
            second = s[len(s)//2:][::-1]
            count = 0
            for i in range(0,len(first)):
                if (first[i] == '(' and second[i] == ')') or (first[i] == '{' and second[i] == '}') or (first[i] == '[' and second[i] == ']'):
                        count+=1    
            if count == len(first):
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

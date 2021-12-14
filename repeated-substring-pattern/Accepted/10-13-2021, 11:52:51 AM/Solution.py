// https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for n in range(2,length+1):
            if length%(n-1) == 0:
                print("111")
                sub = s[0:n-1]
                slist = s.split(sub)
                s2 = set(slist)
                if len(s2) == 1:
                    return True
        return False

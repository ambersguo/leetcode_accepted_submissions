// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if not s:
                return c
            elif c not in s:
                return c
            else:
                s = s.replace(c,'',1)

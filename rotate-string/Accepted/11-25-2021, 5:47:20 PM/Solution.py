// https://leetcode.com/problems/rotate-string

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            first = s[0]
            rest = s[1:]
            new_s = rest + first
            s = new_s
            if s == goal:
                return True
        return False

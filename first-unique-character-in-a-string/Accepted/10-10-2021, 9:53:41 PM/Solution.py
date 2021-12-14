// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            s2 = s.replace(s[i],'',1)
            if s[i] not in s2:
                return i
        return -1

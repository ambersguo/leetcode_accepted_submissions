// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s = s.split()
        if list_s:
            return len(list_s[-1])
        else:
            return 0
        
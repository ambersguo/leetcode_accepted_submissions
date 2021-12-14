// https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            if needle in haystack:
                needle_index = haystack.find(needle)
            else:
                needle_index = -1
        else:
            needle_index = 0
        return needle_index
        
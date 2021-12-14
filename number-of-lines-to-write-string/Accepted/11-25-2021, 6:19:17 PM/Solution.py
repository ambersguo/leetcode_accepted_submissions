// https://leetcode.com/problems/number-of-lines-to-write-string

import string
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        letters = string.ascii_lowercase[:26]
        letter2width = {}
        total = 0
        line = 1
        result = []
        for i in range(26):
            letter2width[letters[i]] = widths[i]
        for c in s:
            width = letter2width[c]
            total += width
            if total > 100:
                total = width
                line += 1
        result.append(line)
        result.append(total)
        return result

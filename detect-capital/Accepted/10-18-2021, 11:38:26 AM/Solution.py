// https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        check = 0
        upper_count = 0
        count = 0
        for l in word:
            count += 1
            if l == l.upper():
                upper_count += 1
                if count == 1:
                    check = 1
        if upper_count:
            if check:
                if upper_count == 1 or upper_count == len(word):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True

// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r, oneWrong):
            if l == r:
                return True 
            while l < r:
                if s[l] != s[r]:
                    if oneWrong:
                        return False
                    else:
                        # abbab -> return isValid(bbab) or isValid(abba)
                        return isValid(l+1, r, True) or isValid(l, r-1, True)        
                l += 1
                r -= 1 
            return True

        return isValid(0, len(s) - 1, False)

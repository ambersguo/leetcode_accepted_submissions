// https://leetcode.com/problems/reverse-only-letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i2c ={}
        letters = []
        s_rlist = []
        
        for i in range(len(s)):
            i2c[i] = s[i]
            if s[i].isalpha():
                letters.append(s[i])
        letters_r = letters[::-1]
        
        for i in range(len(s)):
            if i2c[i].isalpha():
                s_rlist.append(letters_r.pop(0))
            else:
                s_rlist.append(i2c[i])
                
        s_r = ''.join(s_rlist)
        return s_r

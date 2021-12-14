// https://leetcode.com/problems/unique-morse-code-words

import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = string.ascii_lowercase[:26]
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter2code = {}
        trans = []
        for i in range(26):
            letter2code[letters[i]] = codes[i]
        for word in words:
            codes = ''
            for l in word:
                code = letter2code[l]
                codes += code
            trans.append(codes)
        trans_set = set(trans)
        return len(trans_set)

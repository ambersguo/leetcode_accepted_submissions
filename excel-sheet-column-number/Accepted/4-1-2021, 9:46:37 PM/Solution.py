// https://leetcode.com/problems/excel-sheet-column-number

from string import ascii_uppercase

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = ascii_uppercase
        letter2num = {}
        n = 1
        for letter in letters:
            letter2num[letter] = n
            n+=1

        nall = 0
        count = len(columnTitle)-1
        for letter in columnTitle:
            num = letter2num[letter]
            nall = nall + num*(26**count)
            count = count -1
        return nall

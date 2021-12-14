// https://leetcode.com/problems/excel-sheet-column-title

from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = ascii_uppercase
        num2letter = {}
        n = 1
        for letter in letters:
            num2letter[n] = letter
            n+=1

        lall = ""
        while columnNumber >= 1:
            num = int(columnNumber)%26
            if num == 0:
                l = num2letter[26]
                columnNumber = columnNumber -26
            else:
                l = num2letter[num]
            lall = lall + l
            columnNumber = columnNumber/26
        lall = lall[::-1]
        return lall

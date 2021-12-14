// https://leetcode.com/problems/keyboard-row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        first = first + first.upper()
        second = second + second.upper()
        third = third + third.upper()
        ans = []
        for w in words:
            check = 0
            tag = 0
            last_tag = 0
            count = 0
            for l in w:
                if l in first:
                    tag = 1
                elif l in second:
                    tag = 2
                elif l in third:
                    tag = 3
                else:
                    check = 1
                    break
                count += 1
                if tag != last_tag and count>1:
                    check = 1
                    break
                last_tag = tag
            if not check:
                ans.append(w)
        return ans

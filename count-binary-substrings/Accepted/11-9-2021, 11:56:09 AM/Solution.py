// https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        index2num = {}
        diff = []
        count = 0
        left = right = ''
        for i in range(len(s)):
            index2num[i] = s[i]
            if i > 0 and s[i] != s[i-1]:
                diff.append(i)
        for i in diff:
            count += 1
            right = index2num[i]
            left = index2num[i-1]
            j = i-1
            while j >= 1 and i <= len(s)-2:
                i += 1
                j -= 1
                if index2num[i] == right and index2num[j] == left:
                    count += 1
                else:
                    break
        return count

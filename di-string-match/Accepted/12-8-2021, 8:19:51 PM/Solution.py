// https://leetcode.com/problems/di-string-match

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        left = 0
        right = n
        perm = []
        for c in s:
            if c == 'I':
                perm.append(left)
                left += 1
            else:
                perm.append(right)
                right -=1
        if s[-1] == 'I':
            perm.append(left)
        else:
            perm.append(right)
        return perm

// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char2index1 = {}
        char2index2 = {}
        set1 = ()
        set2 = ()
        if len(s) == len(t):
            for i in range(len(s)):
                char2index1.setdefault(s[i],[]).append(i)
                char2index2.setdefault(t[i],[]).append(i)
            set1 = set(tuple(x) for x in char2index1.values())
            set2 = set(tuple(x) for x in char2index2.values())
            if set1 == set2:
                return True
            else:
                return False
        else:
            return False

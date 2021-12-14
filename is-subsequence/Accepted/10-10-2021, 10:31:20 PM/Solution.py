// https://leetcode.com/problems/is-subsequence

import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = 0
        for c in s:
            mark = 0
            if c not in t:
                return False
            else:
                if not check:
                    pre = t.index(c)
                    check+=1
                else:
                    indice = [i.start() for i in re.finditer(c, t)]
                    for index in indice:
                        if index <= pre:
                            if len(indice) == 1:
                                return False
                            else:
                                next
                        else:
                            pre = index
                            mark = 1
                            break
                    if not mark:
                        return False
        return True

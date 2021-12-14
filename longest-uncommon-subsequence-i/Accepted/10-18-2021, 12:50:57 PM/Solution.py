// https://leetcode.com/problems/longest-uncommon-subsequence-i

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        if len(a) > len(b):
            longer = len(a)
        else:
            longer = len(b)
        if a in b or b in a:
            return longer
        for l in a:
            if l not in b:
                return longer
        pre_index = -1
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    if pre_index > j:
                        return longer
                    elif pre_index == j:
                        b = b.replace(b[j],'',1)
                        if a[i] not in b:
                            return longer
                    pre_index = j
                    break
        return -1

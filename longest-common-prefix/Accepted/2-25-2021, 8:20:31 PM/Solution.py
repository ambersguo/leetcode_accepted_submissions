// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs:
            n = len(min(strs,key=len))
            for i in range(0, n):
                set_pop = set(map(lambda x: x[i], strs))
                if len(set_pop) == 1:
                    prefix = prefix + list(set_pop)[0]
                    i+=1
                else:
                    break
        return prefix
        
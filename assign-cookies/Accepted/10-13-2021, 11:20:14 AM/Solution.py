// https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = count = 0
        while i<len(g) and g and s:
            if s[0] >= g[i]:
                g.pop(i)
                s.pop(0)
                count+=1
            else:
                i+=1
        return count

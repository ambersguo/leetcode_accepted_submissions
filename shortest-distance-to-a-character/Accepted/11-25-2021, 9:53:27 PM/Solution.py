// https://leetcode.com/problems/shortest-distance-to-a-character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indice = []
        result = []
        for i in range(len(s)):
            if s[i] == c:
                indice.append(i)
        for i in range(len(s)):
            dislist = []
            for j in indice:
                dis = abs(i-j)
                dislist.append(dis)
            dismin = min(dislist)
            result.append(dismin)
        return result

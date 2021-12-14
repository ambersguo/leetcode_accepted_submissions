// https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
    def countSegments(self, s: str) -> int:
        n = 0
        if len(s):
            slist = s.split(" ")
            for ele in slist:
                if ele:
                    n+=1
            return n
            
        else:
            return 0

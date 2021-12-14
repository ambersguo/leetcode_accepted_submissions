// https://leetcode.com/problems/construct-the-rectangle

import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(math.sqrt(area))
        while mid:
            if area%mid == 0:
                n = int(area/mid)
                return [n,mid]
            else:
                mid -=1

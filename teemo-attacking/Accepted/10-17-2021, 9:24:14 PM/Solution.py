// https://leetcode.com/problems/teemo-attacking

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        last_end = -1
        last_t = -1
        for t in timeSeries:
            if t > last_end:
                total += duration
            else:
                total += t - last_t  
            last_end = t + duration - 1
            last_t = t
        return total

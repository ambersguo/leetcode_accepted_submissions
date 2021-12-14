// https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        if guess(start) == 0:
            return start
        elif guess(end) == 0:
            return end
        else:
            while start < end:
                mid = int((start+end)/2)
                if guess(mid) == 0:
                    return mid
                elif guess(mid) == -1:
                    end = mid
                    if end == n:
                        return start
                elif guess(mid) == 1:
                    start = mid
                    if start == 1:
                        return n
            return start

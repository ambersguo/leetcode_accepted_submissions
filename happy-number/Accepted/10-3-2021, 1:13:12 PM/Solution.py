// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        nlist = list(map(int, str(n)))
        sum_of_squares = sum(map(lambda x:x*x, nlist))
        sumlist = []
        while sum_of_squares:
            sum_of_squares = sum(map(lambda x:x*x, nlist))
            nlist = list(map(int, str(sum_of_squares)))
            if sum_of_squares in sumlist:
                return False
            elif sum_of_squares == 1:
                return True
            else:
                sumlist.append(sum_of_squares)

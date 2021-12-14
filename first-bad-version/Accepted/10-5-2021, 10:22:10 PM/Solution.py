// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            while n > 1:
                if isBadVersion(n-1):
                    n = n-1
                else:
                    break
            return n
        else:
            start = 1
            end = n
            while end-start > 1:
                if isBadVersion((start+end)/2):
                    end = int((start+end)/2)
                else:
                    start = int((start+end)/2 + 1)
            if isBadVersion(start):
                return start
            else:
                return start + 1

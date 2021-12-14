// https://leetcode.com/problems/positions-of-large-groups

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        pre = ''
        intervals = []
        start2end = {}
        starts = []
        large = []
        for i in range(len(s)):
            c = s[i]
            if c != pre:
                end = i-1
                if end >= 0:
                    intervals.append([start,end])
                start = i
            pre = s[i]
        intervals.append([start, len(s)-1])
        for [start, end] in intervals:
            if end - start >= 2:
                start2end[start] = end
                starts.append(start)
        starts.sort()
        for start in starts:
            end = start2end[start]
            large.append([start, end])
        return large

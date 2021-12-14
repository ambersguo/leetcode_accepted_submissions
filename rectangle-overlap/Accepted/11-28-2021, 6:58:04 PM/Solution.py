// https://leetcode.com/problems/rectangle-overlap

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[2] > rec2[2]:
            rec_right = rec1[:]
            rec_left = rec2[:]
        else:
            rec_right = rec2[:]
            rec_left = rec1[:]
        
        if rec_left[2] > rec_right[0] and rec_left[3] > rec_right[1] and rec_left[1] < rec_right[3] and rec_left[0] < rec_right[2]:
            return True
        else:
            return False

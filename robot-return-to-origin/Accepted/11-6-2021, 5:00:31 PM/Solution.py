// https://leetcode.com/problems/robot-return-to-origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ucount = dcount = lcount = rcount = 0
        for move in moves:
            if move == 'U':
                ucount += 1
            elif move == 'D':
                dcount += 1
            elif move == 'L':
                lcount += 1
            else:
                rcount += 1
        if ucount == dcount and lcount == rcount:
            return True
        else:
            return False

// https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        count_L = 0
        L_pre = -1
        for i in range(len(s)):
            if s[i] == 'A':
                count_A += 1
            elif s[i] == 'L':
                if L_pre == -1:
                    count_L = 1
                elif i - L_pre == 1:
                    count_L += 1
                elif i - L_pre > 1:
                    count_L = 1
                L_pre = i
                if count_L >2:
                    return False
        if count_A < 2:
            return True
        else:
            return False

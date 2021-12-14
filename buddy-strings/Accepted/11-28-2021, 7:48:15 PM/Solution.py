// https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        else:
            swap = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    swap.append(i)
            
            if len(swap) == 0:
                if len(set(s)) == len(s):
                    return False
                else:
                    return True
            elif len(swap) != 2:
                return False
            else:
                if s[swap[0]] == goal[swap[1]] and s[swap[1]] == goal[swap[0]]:
                    return True
                else:
                    return False

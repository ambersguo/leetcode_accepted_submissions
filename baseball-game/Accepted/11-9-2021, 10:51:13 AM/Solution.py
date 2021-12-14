// https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for s in ops:
            if s.isdigit() or '-' in s:
                records.append(int(s))
            elif s == '+' and len(records) > 1:
                last = int(records[-1]) + int(records[-2])
                records.append(last)
            elif s == 'C' and len(records) > 0:
                records.pop()
            elif s == 'D' and len(records) > 0:
                last = records[-1]
                records.append(int(last)*2)
        total = sum(records)
        return total

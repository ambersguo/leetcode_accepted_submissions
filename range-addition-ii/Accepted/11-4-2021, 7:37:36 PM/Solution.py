// https://leetcode.com/problems/range-addition-ii

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ops_ele_first = []
        ops_ele_second = []
        if ops:
            for ops_ele in ops:
                ops_ele_first.append(ops_ele[0])
                ops_ele_second.append(ops_ele[1])
            total = min(ops_ele_first) * min(ops_ele_second)
        else:
            total = m*n
        return total

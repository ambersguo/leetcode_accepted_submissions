// https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        m = len(strs)
        count = 0
        for i in range(n):
            col = []
            pre = strs[0][i]
            for j in range(m):
                if strs[j][i] < pre:
                    count += 1
                    break
                pre = strs[j][i]

        return count

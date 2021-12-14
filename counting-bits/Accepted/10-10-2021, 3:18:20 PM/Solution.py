// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        ilist = []
        for i in range(n+1):
            bin_i = format(i,'b')
            ilist = map(lambda x: int(x), str(bin_i))
            ans.append(sum(ilist))
        return ans

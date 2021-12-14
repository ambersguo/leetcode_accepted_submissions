// https://leetcode.com/problems/fair-candy-swap

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a_sum = b_sum = 0
        aindex2value = {}
        bindex2value = {}
        for i in range(len(aliceSizes)):
            a_sum += aliceSizes[i]
            aindex2value[i] = aliceSizes[i]
            
        for j in range(len(bobSizes)):
            b_sum += bobSizes[j]

        diff = (a_sum - b_sum)/2
        for b in bobSizes:
            a = int(b + diff)
            if a in aindex2value.values():
                return [a, b]

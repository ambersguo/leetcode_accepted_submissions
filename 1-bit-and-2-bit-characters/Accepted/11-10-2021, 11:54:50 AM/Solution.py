// https://leetcode.com/problems/1-bit-and-2-bit-characters

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.pop(-1)
        i = 0
        while len(bits) > 1:
            if bits[0] == 0:
                bits.pop(0)
            else:
                bits.pop(0)
                bits.pop(0)
        if bits:
            if bits[0] == 1:
                return False
            else:
                return True
        else:
            return True

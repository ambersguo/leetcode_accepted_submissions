// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_bi = str(bin(int(a,2) + int(b,2)))[2:]
        return sum_bi
        
// https://leetcode.com/problems/repeated-dna-sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        repeats = []
        for i in range(len(s)-9):
            ss = s[i:i+10]
            if ss not in seen:
                seen[ss] = i
            else:
                repeats.append(ss)
            i += 1
        uniq_repeats = set(repeats)
        return uniq_repeats

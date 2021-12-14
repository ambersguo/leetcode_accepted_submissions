// https://leetcode.com/problems/license-key-formatting

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s2 = s.replace('-','')
        s2 = s2.upper()
        n = len(s2)%k
        if n == 0:
            first = ""
            new_s = s2
        else:
            first = s2[0:n]
            new_s = s2[n:]
        chunks = [new_s[i:i+k] for i in range(0, len(new_s), k)]
        chunks_join = '-'.join(chunks)
        if chunks_join:
            if first:
                final = first + '-' + chunks_join
            else:
                final = chunks_join
        else:
            final = first
        return final

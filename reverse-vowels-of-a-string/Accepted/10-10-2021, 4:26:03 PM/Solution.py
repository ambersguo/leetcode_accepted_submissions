// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        i = j = 0
        v = []
        indexv2s = {}
        s = list(s)
        str_s = ""
        for c in s:
            if c in ['a','e', 'i', 'o', 'u','A','E','I','O','U']:
                v.append(c)
                indexv2s[j]= i
                j+=1
            i+=1
        n = int(len(v)/2)
        for j in range(n):
            temp = v[j]
            v[j] = v[len(v)-j-1]
            v[len(v)-j-1] = temp
        for j in range(len(v)):
            s[indexv2s[j]] = v[j]
        for c in s:
            str_s += c
        return str_s

// https://leetcode.com/problems/goat-latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        vols = 'aeiouAEIOU'
        wordsnew = []
        for i in range(len(words)):
            word = words[i]
            check = 0
            for v in vols:
                if word.startswith(v):
                    check = 1
            if check:
                word_new = word + 'ma'
            else:
                first = word[0]
                rest = word[1:]
                word_new = rest + first + 'ma'
            for j in range(i+1):
                word_new += 'a'
            wordsnew.append(word_new)
        result = ' '.join(wordsnew)
        return result
 
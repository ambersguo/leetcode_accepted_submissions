// https://leetcode.com/problems/shortest-completing-word

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = ''
        words_sorted = []
        check = 1
        min_word = ''
        for c in licensePlate:
            if c.isalpha():
                c = c.lower()
                letters += c
        for word in words:
            count = 0
            word_constant = word
            for l in letters:
                if l in word:
                    word = word.replace(l,'',1)
                    count += 1
            if count == len(letters):
                if check:
                    check = 0
                    min_word = word_constant
                    min_len = len(word_constant)
                else:
                    if len(word_constant) < min_len:
                        min_word = word_constant
                        min_len = len(word_constant)
        return min_word

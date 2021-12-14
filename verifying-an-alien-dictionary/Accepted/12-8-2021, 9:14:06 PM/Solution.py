// https://leetcode.com/problems/verifying-an-alien-dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter2order = {}
        for i in range(len(order)):
            letter2order[order[i]] = i
        for word in words:
            if word == words[0]:
                pre = word
                next
            min_len = min(len(word), len(pre))
            check = 0
            for i in range(min_len):
                if letter2order[word[i]] > letter2order[pre[i]]:
                    check = 1
                    break
                elif letter2order[word[i]] == letter2order[pre[i]]:
                    next   
                else:
                    return False
            if not check:
                if len(word) < len(pre):
                    return False
            pre = word
        return True

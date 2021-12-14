// https://leetcode.com/problems/uncommon-words-from-two-sentences

from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split(' ')
        s2_words = s2.split(' ') 
        uncommons = []
        uncommons1 = []
        uncommons2 = []
        word2count1 = defaultdict(int)
        word2count2 = defaultdict(int)

        for word in s1_words:
            word2count1[word] += 1
            if word not in s2_words:
                uncommons1.append(word)

        for word in s2_words:
            word2count2[word] += 1
            if word not in s1_words:
                uncommons2.append(word)

        for word in uncommons1:
            if word2count1[word] == 1:
                uncommons.append(word)
        for word in uncommons2:
            if word2count2[word] == 1:
                uncommons.append(word)

        return uncommons

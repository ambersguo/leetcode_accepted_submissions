// https://leetcode.com/problems/most-common-word

import re
from collections import defaultdict

class Solution:
    from collections import defaultdict
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split('\s|\,|\!|\?|\'|\;|\.', paragraph)
        wordsnew = []
        word2count = defaultdict(int)
        for word in words:
            if word:
                word = word.lower()
                wordsnew.append(word)
        for word in wordsnew:
            if word not in banned:
                word2count[word] += 1
        result = max(word2count, key=word2count.get)
        return result

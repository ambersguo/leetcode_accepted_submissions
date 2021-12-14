// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        patterns = list(pattern)
        pattern2word = {}
        uniq_pattern = []
        uniq_word = []
        if len(patterns) == len(words):
            for i in range(len(patterns)):
                if patterns[i] not in uniq_pattern:
                    if words[i] not in uniq_word:
                        pattern2word[patterns[i]] = words[i]
                        uniq_pattern.append(patterns[i])
                        uniq_word.append(words[i])
                    else:
                        return False
                else:
                    if pattern2word[patterns[i]] != words[i]:
                        return False
                    else:
                        next
            return True
        else:
            return False

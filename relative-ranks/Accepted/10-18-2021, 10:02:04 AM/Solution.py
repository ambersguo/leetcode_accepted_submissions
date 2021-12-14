// https://leetcode.com/problems/relative-ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = score[:]
        score_sorted.sort(reverse=True)
        score2rank = {}
        ranks = []
        for i in range(len(score_sorted)):
            if i == 0:
                score2rank[score_sorted[i]] = "Gold Medal"
            elif i == 1:
                score2rank[score_sorted[i]] = "Silver Medal"
            elif i == 2:
                score2rank[score_sorted[i]] = "Bronze Medal"
            else: 
                score2rank[score_sorted[i]] = str(i + 1)
        for s in score:
            rank = score2rank[s]
            ranks.append(rank)
        return ranks

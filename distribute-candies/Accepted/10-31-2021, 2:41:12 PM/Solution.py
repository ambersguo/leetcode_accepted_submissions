// https://leetcode.com/problems/distribute-candies

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = len(set(candyType))
        num = len(candyType)/2
        eat = int(min(types, num))
        return eat

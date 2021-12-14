// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # to get to the top
        cost.append(0)
        # base cases
        mc = [0, 0]
        # dp solution
        for i in range(2, len(cost)):
            mc.append(min(mc[-1] + cost[i - 1], mc[-2] + cost[i - 2]))
        return mc[-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = [0] * len(cost)
        for i in range(2, len(cost)):
            minCosts[i] = min(cost[i-1] + minCosts[i-1], cost[i-2] + minCosts[i-2])
        return min(cost[-1] + minCosts[-1], cost[-2] + minCosts[-2])     
        
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            weight1 = heapq.heappop(stones)
            weight2 = heapq.heappop(stones)
            if weight1 != weight2:
                heapq.heappush(stones, weight1 - weight2)
        if stones:
            return -stones[0]
        return 0


        
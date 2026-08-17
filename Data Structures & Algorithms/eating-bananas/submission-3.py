import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = r
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours > h:
                l = k+1
            else:
                r = k-1
                output = k
        return output


        
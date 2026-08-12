class Solution:
    def climbStairs(self, n: int) -> int:
        distinct = [1] * (n+1)
        for i in range(2, len(distinct)):
            distinct[i] = distinct[i-1] + distinct[i-2]
        return distinct[n]
        
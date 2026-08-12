class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 100000
        for price in prices:
            minPrice = min(price, minPrice)
            currentProfit = price - minPrice
            maxProfit = max(maxProfit, currentProfit)
        return maxProfit

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentProfit = 0
        i = 0
        while i < len(prices):
            j = i
            while j < len(prices)-1 and prices[j] >= prices[i]:
                j += 1
                if prices[j] - prices[i] > currentProfit:
                    currentProfit = prices[j] - prices[i]
            if maxProfit < currentProfit:
                maxProfit = currentProfit
            i+=1
        return maxProfit
            
        
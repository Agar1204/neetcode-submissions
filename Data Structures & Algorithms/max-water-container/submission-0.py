class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        left = 0
        right = len(heights)-1
        while left < right:
            amount = min(heights[left], heights[right]) * (right-left)
            maxAmount = max(amount, maxAmount)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return maxAmount
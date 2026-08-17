class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1
        
        currIndex = 0
        for i in range(len(colors)):
            for j in range(colors[i]):
                nums[currIndex] = i
                currIndex+=1

        
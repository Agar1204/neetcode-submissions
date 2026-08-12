class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        res = 1

        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                currentIndex = nums[i]+1
                currentStreak = 1
                while res < len(nums):
                    if currentIndex in num_set:
                        currentIndex+=1
                        currentStreak+=1
                    else:
                        break
                    if currentStreak > res:
                        res = currentStreak
        return res

        

        
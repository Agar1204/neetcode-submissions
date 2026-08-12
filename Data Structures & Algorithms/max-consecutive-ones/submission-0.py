class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                curr = 0
            if curr > max:
                max = curr
        return max
        
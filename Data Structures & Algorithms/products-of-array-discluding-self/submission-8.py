class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1, 1, 2, 8]
        # suffix = [48, 24, 6, 1] -> [1, 6, 24, 48]
        prefix = []
        suffix = []
        prefix.append(1)
        suffix.append(1)
        for i in range(len(nums)-1):
            prefix.append(nums[i] * prefix[i])
            suffix.append(nums[len(nums)-1-i]*suffix[i])
        
        index = 0
        res = []
        while index < len(nums):
            res.append(prefix[index] * suffix[len(nums)-index-1])
            index+=1
        return res

            
        
        
        
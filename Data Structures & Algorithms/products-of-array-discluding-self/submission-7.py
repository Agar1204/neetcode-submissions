class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        # [1, -1, 0, 0, 0]
        # [0, 6, 6, 3, 1]
        prefix = []
        suffix = []
        prefix.append(1)
        suffix.append(1)
        for i in range(len(nums)-1):
            prefix.append(nums[i] * prefix[len(prefix) - 1])
        
        for i in range(len(nums)-1, 0, -1):
            suffix.append(nums[i] * suffix[len(suffix)-1])
        
        output = []
        start, end = 0, len(nums) - 1
        while start < len(nums) and end > -1:
            output.append(prefix[start] * suffix[end])
            start += 1
            end -= 1
        return output
            
        
        
        
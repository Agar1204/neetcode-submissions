class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        def dfs(i, remaining):
            if remaining == 0:
                output.append(subset.copy())
                return 
            
            if i >= len(nums) or remaining < 0:
                return 
            
            # Include nums[i]
            subset.append(nums[i])
            dfs(i, remaining - nums[i])
            subset.pop()

            # Don't include nums[i]
            dfs(i+1, remaining)
        dfs(0, target)
        return output

            



        
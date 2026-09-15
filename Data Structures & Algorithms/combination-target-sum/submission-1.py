class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(index, target):
            if target == 0:
                result.append(subset[:])
                return
            if index >= len(nums) or target < 0:
                return

            subset.append(nums[index])
            backtrack(index, target - nums[index])
            
            subset.pop()
            backtrack(index+1, target)

        backtrack(0, target)
        return result

                
        
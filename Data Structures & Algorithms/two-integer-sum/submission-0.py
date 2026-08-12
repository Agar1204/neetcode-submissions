class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        output = []
        for i in range(len(nums)):
            if nums[i] in remaining:
                output.append(remaining[nums[i]])
                output.append(i)
                return output
            else:
                remaining[target-nums[i]] = i
        return output

        
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in reversed(range(len(arr))):
            curr = arr[i]
            arr[i] = max
            if curr > max:
                max = curr
        return arr
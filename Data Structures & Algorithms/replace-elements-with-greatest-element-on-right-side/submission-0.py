class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        for i in reversed(range(len(arr))):
            if i == len(arr)-1:
                max = arr[-1]
                arr[-1] = -1
                continue
            newMax = max
            if arr[i] > max:
                newMax = arr[i]
            arr[i] = max
            max = newMax
        return arr

        
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs) // 2
        leftArray = self.mergeSort(pairs[:m])
        rightArray = self.mergeSort(pairs[m:])

        return self.merge(leftArray, rightArray)

    def merge(self, left, right):
        l = 0
        r = 0
        output = []
        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                output.append(left[l])
                l += 1
            else:
                output.append(right[r])
                r += 1
        while l < len(left):
            output.append(left[l])
            l += 1
        while r < len(right):
            output.append(right[r])
            r += 1
        return output


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def helper(self, start, end, pairs):
        if end - start + 1 <= 1:
            return
        pivot = pairs[end]
        left = start
        for i in range(start, end):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1
        pairs[end] = pairs[left]
        pairs[left] = pivot
        self.helper(start, left -1, pairs)
        self.helper(left + 1, end, pairs)
        return

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(0, len(pairs)-1, pairs)
        return pairs

    
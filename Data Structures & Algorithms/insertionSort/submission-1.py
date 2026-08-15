# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        lists = []
        lists.append(list(pairs))
        for i in range(1, len(pairs)):
            pairs_list = list(lists[-1])
            j = i - 1
            while j >= 0 and pairs_list[j].key > pairs_list[j+1].key:
                temp = pairs_list[j+1]
                pairs_list[j+1] = pairs_list[j]
                pairs_list[j] = temp
                j-=1
            lists.append(pairs_list)
        return lists

        
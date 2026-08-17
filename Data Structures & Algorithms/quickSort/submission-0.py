class Solution:

    def sort_helper(self, pairs, low, high):
        if low < high:
            partition_index = self.partition(pairs, low, high)
            self.sort_helper(pairs, low, partition_index-1)
            self.sort_helper(pairs, partition_index+1, high)

    def partition(self, pairs, low, high):

        if high - low <= 0:
            return high
            
        swapIndex = low
        currentIndex = low
        pivot = pairs[high]

        while currentIndex < high:
            if pairs[currentIndex].key < pivot.key:
                temp = pairs[currentIndex]
                pairs[currentIndex] = pairs[swapIndex]
                pairs[swapIndex] = temp
                swapIndex += 1
            currentIndex += 1
        
        temp = pairs[swapIndex]
        pairs[swapIndex] = pairs[high]
        pairs[high] = temp
        return swapIndex

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort_helper(pairs, 0, len(pairs)-1)
        return pairs
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        output = []
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        sorted_frequencies = sorted(frequencies, key = frequencies.get, reverse=True)

        print(sorted_frequencies)
        return sorted_frequencies[:k]
        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        output = []
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1])
        k_sorted_frequencies = sorted_frequencies[len(sorted_frequencies)-k:]

        for ans in k_sorted_frequencies:
            output.append(ans[0])
        return output
        
        
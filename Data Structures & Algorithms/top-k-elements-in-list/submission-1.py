class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} # Key is a number, value is # of times it shows up
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        result = []
        sorted_d = sorted(d, key = d.get, reverse=True)
        return sorted_d[0:k]
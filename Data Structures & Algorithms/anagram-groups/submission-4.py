class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = {}
        res = []
        if len(strs) == 1:
            res.append(strs)
            return res

        characters = "abcdefghijklmnopqrstuvwxyz"
        chars_dict = {}
        for i in range(len(characters)):
            chars_dict[characters[i]] = i

        for s in strs:
            s_frequency = [0] * 26
            for ch in s:
                s_frequency[chars_dict[ch]] += 1
            hashable_freq = tuple(s_frequency)
            if hashable_freq not in frequencies:
                frequencies[hashable_freq] = []
            frequencies[hashable_freq].append(s)
        return list(frequencies.values())
            
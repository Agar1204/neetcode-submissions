class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary with key being frequencies and value being list of words
        frequencies = {}
        output = []
        if len(strs) == 1:
            output.append(strs)
            return output
        
        characters = "abcdefghijklmnopqrstuvwxyz"
        chars_dict = {}
        for i in range(len(characters)):
            if characters[i] not in chars_dict:
                chars_dict[characters[i]] = i
        
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[chars_dict[ch]] += 1
            hashed_freq = tuple(freq)
            if hashed_freq not in frequencies:
                frequencies[hashed_freq] = []
            frequencies[hashed_freq].append(s)
        return list(frequencies.values())
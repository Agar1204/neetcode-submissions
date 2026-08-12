class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        if len(strs) == 1:
            output.append(strs)
            return output

        group_frequencies = {}
        characters = "abcdefghijklmnopqrstuvwxyz"
        
        chars_dict = {}
        for i in range(len(characters)):
            chars_dict[characters[i]] = i
        
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[chars_dict[ch]] += 1
            hashed_freq = tuple(freq)
            if hashed_freq not in group_frequencies:
                group_frequencies[hashed_freq] = []
            group_frequencies[hashed_freq].append(s)
        
        for group in group_frequencies:
            output.append(group_frequencies[group])
        return output

               

        

        

        
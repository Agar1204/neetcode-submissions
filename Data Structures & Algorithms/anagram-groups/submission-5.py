class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        output = []
        characters = "abcdefghijklmnopqrstuvwxyz"
        character_mappings = {}
        for i in range(len(characters)):
            character_mappings[characters[i]] = i

        anagrams = {}
        for s in strs:
            indices = [0]*26
            for ch in s:
                index = character_mappings[ch]
                indices[index] += 1
            mapping = tuple(indices)
            if mapping not in anagrams:
                anagrams[mapping] = []
            anagrams[mapping].append(s)
        for anagram in anagrams:
            output.append(anagrams[anagram])
        return output


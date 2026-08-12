class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # key = count of each letter, value = list of anagrams
        for s in strs:
            count = [0] * 26 # Stores count of each letter a-z
            for ch in s:
                count[ord(ch) - ord("a")] += 1 #a in 0, b in 1, c in 2 index
            count = tuple(count) #key cannot be a list
            if count not in result:
                print("hi")
                result[count] = []
            result[count].append(s)
        return result.values()
            
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequencies = {}
        t_frequencies = {}
        for ch_s in s:
            if ch_s not in s_frequencies:
                s_frequencies[ch_s] = 0
            s_frequencies[ch_s] += 1
        
        for ch_t in t:
            if ch_t not in t_frequencies:
                t_frequencies[ch_t] = 0
            t_frequencies[ch_t] += 1
        return s_frequencies == t_frequencies
        
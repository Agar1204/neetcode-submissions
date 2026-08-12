class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = {}
        t_chars = {}
        for i in range(len(s)):
            if s[i] not in s_chars:
                s_chars[s[i]] = 0
            s_chars[s[i]] += 1
            if t[i] not in t_chars:
                t_chars[t[i]] = 0
            t_chars[t[i]] += 1
        return t_chars == s_chars
        
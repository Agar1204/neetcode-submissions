class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        l = 0
        r = len(s)-1
        print(s)
        while l < r:
            while l < r and not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while l < r and not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            l += 1
            r -= 1
        return True
        
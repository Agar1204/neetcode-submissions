class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedS = s.strip()
        inputStr = ""
        for ch in strippedS:
            if ch.isalpha() or ch.isnumeric():
                inputStr += ch.lower()
        
        left = 0
        right = len(inputStr) - 1
        while left <= right:
            if inputStr[left] != inputStr[right]:
                return False
            left+=1
            right-=1
        return True
        
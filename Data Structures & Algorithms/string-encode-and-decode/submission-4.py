class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(strs)):
            output += "#*" + strs[i]
        return output

 #. #*neet#*code#*love#*you
    def decode(self, s: str) -> List[str]:
        words = s.split("#*")
        return words[1:]

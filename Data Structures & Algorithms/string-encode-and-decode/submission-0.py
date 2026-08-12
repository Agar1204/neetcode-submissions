class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += s + "/0"
        return output

    def decode(self, s: str) -> List[str]:
        strs = s.split("/0")
        return strs[:len(strs)-1]
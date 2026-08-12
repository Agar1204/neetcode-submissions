class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = "({["
        closed_brackets = ")}]"
        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            elif ch in closed_brackets:
                index = closed_brackets.index(ch)
                if len(stack) == 0 or open_brackets[index] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
        return len(stack) == 0
        
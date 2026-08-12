class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current = 0
        stack = []
        for i in range(len(tokens)):
            try:
                tokensValue = int(tokens[i])
                stack.append(tokensValue)
            except ValueError:
                first = stack.pop(-1)
                second = stack.pop(-1)
                if tokens[i] == "+":
                    stack.append(second + first)
                elif tokens[i] == "-":
                    stack.append(second - first)
                elif tokens[i] == "/":
                    stack.append(int(second / first))
                else:
                    stack.append(second * first)
        return stack[-1]


        
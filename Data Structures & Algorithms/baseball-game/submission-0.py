class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                sum+=stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif operations[i] == "D":
                sum+=2*stack[-1]
                stack.append(2*stack[-1])
            elif operations[i] == "C":
                sum-=stack[-1]
                stack.pop(-1)
            else:
                sum += int(operations[i])
                stack.append(int(operations[i]))
        return sum
        
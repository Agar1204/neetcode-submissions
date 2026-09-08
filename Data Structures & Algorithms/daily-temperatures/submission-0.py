class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            count = 1
            while stack and temperatures[i] > stack[-1][0]:
                sol[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                count += 1
            stack.append((temperatures[i], i))
        return sol
            

            

        
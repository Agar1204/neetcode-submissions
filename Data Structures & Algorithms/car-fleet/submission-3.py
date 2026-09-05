class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = {}
        for i in range(len(position)):
            indices[position[i]] = i

        position.sort()
        stack = []
        for pos in position: 
            time_steps = (target - pos) / speed[indices[pos]]
            while stack and time_steps >= stack[-1]:
                stack.pop()
            stack.append(time_steps)
        return len(stack)
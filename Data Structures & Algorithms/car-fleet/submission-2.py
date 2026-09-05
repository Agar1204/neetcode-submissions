import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = {}
        for i in range(len(position)):
            indices[position[i]] = i

        position.sort()
        stack = []
        for pos in position: 
            time_steps = (target - pos) / speed[indices[pos]]
            final_position = pos + time_steps * speed[indices[pos]]
            while stack and (time_steps > stack[-1][0] or (time_steps == stack[-1][0] and final_position <= stack[-1][1])):
                stack.pop()
            stack.append((time_steps, final_position))
        return len(stack)

        # 5 26 18 25 9 21 22 12 19 6.   target = 31
        # 7  6  6  4 3  4  9  7 6 4

        # 5  6 9 12 18 19 21 22 25 26
        # 4  7 8  3 3. 2. 3. 1. 2   1
        # 33 34 33 33 36 31 33 31 33 32

        # stack = [(8, 33), (3, 33), (3, 33), (2, 33), (1, 32)]
        # 12 -> 19 -> 26 -> 33
        # 18 -> 24 -> 30 -> 36
        # 19 -> 25 -> 31
        # 21 -> 25 -> 29 -> 33

        








        
        
        
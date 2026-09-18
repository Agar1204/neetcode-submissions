import math 
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 1. Calculate distance of each point and keep a maxheap of size k. add a point only if its closer
        # than the root. Store indices in a hashmap
        # 2. pop each element off a store them in a list

        # Time complexity : k log k
        heap = []
        for i in range(len(points)):
            dist = -1 * math.sqrt((0-points[i][0])**2 + (0-points[i][1])**2)
            if len(heap) < k:
                heapq.heappush(heap, (dist, i))
            elif dist > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (dist, i))
        # heap: -2, -2, 
        output = []
        while heap:
            index = heapq.heappop(heap)[1]
            output.append(points[index])
        return output


        

        
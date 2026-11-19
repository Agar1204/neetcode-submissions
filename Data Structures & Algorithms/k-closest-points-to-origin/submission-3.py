import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)         
            dists.append((dist, point))
        heapq.heapify(dists)
        output = []
        for _ in range(k):
            output.append(heapq.heappop(dists)[1])
        return output
        
        

        
        
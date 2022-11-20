class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dist = []
        # for x, y in points:
        #     dist.append(x ** 2  + y ** 2)
        # argsort = sorted([i for i in range(len(dist))], key=lambda x: dist[x])
        # points = [points[i] for i in argsort]
        # return points[:k]
    
        heap = []
        for x, y in points:
            dist = - (x ** 2  + y ** 2)
            if len(heap) == k:
                heapq.heappush(heap, (dist, x, y))
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x,y) for (dist,x, y) in heap]
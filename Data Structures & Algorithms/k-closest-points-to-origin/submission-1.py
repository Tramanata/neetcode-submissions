class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        def distance(x, y):
            return -(x**2 + y**2)

        for x,y in points:
            heapq.heappush(maxHeap, [distance(x,y), x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []

        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        
        return res
        

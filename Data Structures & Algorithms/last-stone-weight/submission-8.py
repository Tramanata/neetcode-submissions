class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        def smash(x, y):
            res = (-x) - (-y)

            if res == 0:
                return 0 
            return -res


        rocks = [-x for x in stones]
        heapq.heapify(rocks)
        while len(rocks) > 1:
            l = heapq.heappop(rocks)
            r = heapq.heappop(rocks)

            ans = smash(l, r)
            if ans != 0:
                heapq.heappush(rocks, ans)
        
        if len(rocks) == 0:
            return 0    
        return -rocks[0]
            
        def smash(x, y):
            res = x + y

            if res > 0:
                return -res
            elif res < 0:
                return res
            else:
                return 0 
        
class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        res = 0

        while l <= h:
            m = (l + h) // 2

            if m * m > x:
                h = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m
        return res
                
        
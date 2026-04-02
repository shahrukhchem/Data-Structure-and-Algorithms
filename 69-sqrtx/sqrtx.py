class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x
        while l<=r:
            m=l+((r-l)//2)
            square=m**2
            if square==x:
                return m
            elif square<x:
                l=m+1
            else:
                r=m-1
        return l-1

        
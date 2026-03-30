class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(c ** 0.5)
        while l<=r:
            k=l*l+r*r
            if k==c:
                return True
            elif k>c:
                r=r-1
            else:
                l=l+1
        return False
        
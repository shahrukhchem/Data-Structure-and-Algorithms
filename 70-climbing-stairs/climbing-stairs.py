class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            numbertype=[0]*n
            numbertype[0]=1
            numbertype[1]=2
            for i in range(2,n):
                numbertype[i]=numbertype[i-1]+numbertype[i-2]
            return numbertype[n-1]
        
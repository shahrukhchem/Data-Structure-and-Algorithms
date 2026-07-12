class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        compatiblesum=0
        for x in range(1,n+k+1):
            currk=abs(n-x)
            if (currk<=k) and ((n & x) == 0):
                compatiblesum+=x
        return compatiblesum

        
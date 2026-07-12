class Solution:
    def tribonacci(self, n: int) -> int:
        k=n+1
        tribo=[0]*38
        
        tribo[0]=0
        tribo[1]=1
        tribo[2]=1
        if n>=3:
            for i in range(3,n+1):
                tribo[i]=tribo[i-3]+tribo[i-2]+tribo[i-1]
        return tribo[n]
        
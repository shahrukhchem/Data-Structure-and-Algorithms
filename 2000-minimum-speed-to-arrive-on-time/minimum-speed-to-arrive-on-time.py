import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        minspeed=1
        maxspeed=10000000
        n=len(dist)
        totaltime=0
        def isspeedpossible(speed):
            totaltime=0
            for i in range(0,n):
                if i<n-1:
                    totaltime+=math.ceil(dist[i]/speed)
                else:
                    totaltime+=dist[i]/speed
            return totaltime<=hour
        ans=-1
        while minspeed<=maxspeed:
                m=minspeed+((maxspeed-minspeed)//2)
                if isspeedpossible(m):
                    ans=m
                    maxspeed=m-1
                else:
                    minspeed=m+1
        return ans


            
        
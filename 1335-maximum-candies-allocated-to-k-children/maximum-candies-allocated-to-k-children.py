class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        totalcandies=sum(candies)
        def ispilesizeallowed(pilesize,candies,k):
            divisor=pilesize
            currsum=0
            for x in candies:
                    currsum += x // divisor
            if currsum>=k:
                    return True
            else:
                    return False

        if totalcandies<k:
            return 0
        else:
            maxpilesizeallowed= max(candies)
            minpilesizeallowed= 1
            while minpilesizeallowed<=maxpilesizeallowed:
                currpilesize=minpilesizeallowed+((maxpilesizeallowed-minpilesizeallowed)//2)
                if ispilesizeallowed(currpilesize,candies,k):
                    minpilesizeallowed=currpilesize+1
                else:
                    maxpilesizeallowed= currpilesize-1
            return maxpilesizeallowed

                
                
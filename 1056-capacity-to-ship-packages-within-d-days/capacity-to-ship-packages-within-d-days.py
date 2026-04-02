class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def iscapacitypossible(capacity,days):
            daycap=0
            d=1
            for i in weights:
                if i > capacity:   # must handle
                    return False
                daycap+=i
                if daycap>capacity:
                    d=d+1
                    daycap=i
            if d<=days:
                return True
            else:
                return False
        l=1
        r=sum(weights)
        while l<=r:
            m=l+((r-l)//2)
            if iscapacitypossible(m,days):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans



        
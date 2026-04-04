class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l=1
        r=max(quantities)
        def shoprecieveamounteachmin(amounteachmin):
            ans=1000000
            storedist=0
            stores_used=0
            for q in quantities:
                stores_used += (q + amounteachmin - 1) // amounteachmin
            return stores_used<=n
        while l<=r:
            m=l+((r-l)//2)
            if shoprecieveamounteachmin(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans
        

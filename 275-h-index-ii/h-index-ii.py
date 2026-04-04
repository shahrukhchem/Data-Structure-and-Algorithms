class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        l=0
        r=n
        ans=0
        def ishpossible(h):
            count=0
            for i in citations:
                if i>=h:
                    count+=1
            return count>=h
        while l<=r:
            m=l+((r-l)//2)
            if ishpossible(m):
                ans=m
                l=m+1
            else:
                r=m-1
        return ans
        
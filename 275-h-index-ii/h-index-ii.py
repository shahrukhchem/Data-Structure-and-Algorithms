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

        for h in range(0,r+1):
            if not ishpossible(h):
                return h-1
        return n
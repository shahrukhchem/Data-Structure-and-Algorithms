class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        indosize=len(s1)
        n=len(s2)
        r=0
        count={}
        countp={}
        for i in range(0,indosize):
            countp[s1[i]] = countp.get(s1[i], 0) + 1
        res=[]
        for l in range(0,n-indosize+1):
            while r-l+1!=indosize+1:
                count[s2[r]] = count.get(s2[r], 0) + 1
                r=r+1   
            if countp==count:
                    return True
            count[s2[l]]=count[s2[l]]-1 
            if count[s2[l]]==0:
                count.pop(s2[l])
        return False
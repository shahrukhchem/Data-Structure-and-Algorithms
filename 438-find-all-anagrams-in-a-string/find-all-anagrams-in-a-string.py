class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        indosize=len(p)
        n=len(s)
        r=0
        count={}
        countp={}
        for i in range(0,indosize):
            countp[p[i]] = countp.get(p[i], 0) + 1
        res=[]
        for l in range(0,n-indosize+1):
            while r-l+1!=indosize+1:
                count[s[r]] = count.get(s[r], 0) + 1
                r=r+1   
            if countp==count:
                    res.append(l)     
            count[s[l]]=count[s[l]]-1 
            if count[s[l]]==0:
                count.pop(s[l])
              
            
        return res
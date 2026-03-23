class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        n=len(s)
        currs=''
        countdic={}
        maxf = 0
        for r  in range(0,n):
            countdic[s[r]] = countdic.get(s[r], 0) + 1
            maxf = max(maxf, countdic[s[r]])
            currs=currs+s[r]
            if (r-l+1)-maxf<=k:
                count=r-l+1  
            else:
                countdic[s[l]]=countdic[s[l]]-1
                l=l+1
                
                
        return count







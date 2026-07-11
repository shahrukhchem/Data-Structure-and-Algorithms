class Solution:
    def countHomogenous(self, s: str) -> int:
        left=0
        n=len(s)
        currdict={}
        ans=0
        for right in range(n):
            t=s[right]
            if t in currdict:
                currdict[t]+=1
            else:
                currdict[t]=1
            while len(currdict)>=2:
                currdict[s[left]]-=1
                if currdict[s[left]]==0:
                    del currdict[s[left]]
                left=left+1
            ans=ans+right-left+1
        MOD = 10**9 + 7
        return ans%MOD
        
        
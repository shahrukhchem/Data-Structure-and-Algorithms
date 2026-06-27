class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        n=len(s)
        currstr={}
        ans=0
        for right in range(n):
            if s[right] in currstr:
                currstr[s[right]] +=1
            else:
                currstr[s[right]]=1
            while currstr[s[right]]>=2:
                currstr[s[left]]-=1
                left=left+1
            ans= max(ans,right-left+1)
        return ans
        
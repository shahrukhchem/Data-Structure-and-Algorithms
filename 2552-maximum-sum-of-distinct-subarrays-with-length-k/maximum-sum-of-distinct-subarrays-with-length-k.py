class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        left=0
        n=len(nums)
        currdict={}
        currsum=0
        ans=0
        for right in range(n):
            t=nums[right]
            currsum+=t
            if t in currdict:
                currdict[t]+=1
            else:
                currdict[t]=1
            while right - left + 1 > k:
                currdict[nums[left]]-=1
                if currdict[nums[left]]==0:
                    del currdict[nums[left]]
                currsum-=nums[left]
                left=left+1
            if right - left + 1 == k and len(currdict) == k:
                ans = max(ans, currsum)
            
        
        return ans
        
        
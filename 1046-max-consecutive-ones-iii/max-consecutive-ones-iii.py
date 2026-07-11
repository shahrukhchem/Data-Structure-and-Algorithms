class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        n=len(nums)
        currzero=0
        ans=0
        for right in range(n):
            if nums[right]==0:
                currzero+=1
            while currzero>k:
                if nums[left]==0:
                    currzero-=1
                left=left+1
            ans=max(ans,right-left+1)
        return ans

        
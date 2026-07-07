class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        n=len(nums)
        currsum=0
        ans=n*2
        for right in range(n):
            currsum+=nums[right]
            print(currsum,ans)
            while currsum>=target:
                ans=min(ans,right-left+1)
                currsum-=nums[left]
                left=left+1
                
        if ans==n*2:
            return 0
        else:
            return ans
        
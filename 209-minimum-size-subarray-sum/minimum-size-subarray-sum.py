class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        n=len(nums)
        minsize=float('inf')
        currsum=nums[l]
        while l<n:
            indosize=r-l+1
            if currsum>=target:
                minsize=min(minsize,indosize)
                currsum=currsum-nums[l]
                l=l+1
            elif  r==n-1:
                currsum=currsum-nums[l]
                l=l+1
            elif currsum<target:
                r=r+1
                currsum=currsum+nums[r]
        if minsize==float('inf'):
            return 0
        return minsize
        
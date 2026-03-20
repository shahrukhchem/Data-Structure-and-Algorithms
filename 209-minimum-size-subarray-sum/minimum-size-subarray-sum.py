class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        n=len(nums)
        minsize=float('inf')
        currsum=nums[l]
        while r<n:
            indosize=r-l+1
            if currsum>=target:
                if minsize>indosize:
                    minsize=indosize
                currsum=currsum-nums[l]
                l=l+1
            else:
                r=r+1
                if r<n:
                    currsum=currsum+nums[r]
        if minsize==float('inf'):
            return 0
        return minsize
        
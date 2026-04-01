class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        n=len(nums)
        count=0
        r=0
        prod=1
        if k <= 1:
            return 0
        for r in range(0,n):
            prod=prod*nums[r]
            while prod>=k:
                prod=prod//nums[l]
                l=l+1 
            count+=(r-l+1)
        return count
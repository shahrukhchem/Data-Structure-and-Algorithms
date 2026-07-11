class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        n=len(nums)
        ans=0
        for right in range(n):
            while  nums[right]==0 and left<=right:
                left=left+1
            ans=max(ans,right-left+1)
        return ans

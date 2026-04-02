class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float('inf')
        l=0
        r=n-1
        while l<=r:
            m=l+((r-l)//2)
            print(l,m,r,ans)
            if nums[l]<=nums[r]:
                ans=min(ans,nums[l])
                return ans
            elif nums[l]<=nums[m]:
                print('onside',ans,nums[m])
                ans=min(ans,nums[l])
                l=m+1
            elif nums[r]>=nums[m]:
                print('inside',ans,nums[m])
                ans=min(ans,nums[m])
                r=m-1
        return ans

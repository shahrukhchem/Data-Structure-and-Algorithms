class Solution:
    def iscurrnumvalid(self,currnums):
        n=len(currnums)
        k=currnums[1]-currnums[0]
        for i in range(2,n):
            if currnums[i]-currnums[i-1]!=k:
                return False
        return True
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l=0
        r=0
        n=len(nums)
        countsubarr=0
        while l<=n-3 :
            print(l,r)
            indosize=r-l+1
            currnums=nums[l:r+1]
            if indosize<3:
                    r=r+1
            else:
                currnums=nums[l:r+1]
                if self.iscurrnumvalid(currnums):
                    countsubarr=countsubarr+1
                    r=r+1
                    if r==n:
                        l=l+1
                        r=l
                else:
                    l=l+1
                    r=l

        return countsubarr
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        r=sum(nums)
        l=max(nums)
        def numberofsubarrayforfixsum(fixsum):
            nosa=0
            currsum=0
            minsumsubarray=-1
            for i in nums:
               # print(i,currsum,minsumsubarray,nosa)
                if i >fixsum:
                    return 0
                if currsum+i<fixsum:
                    currsum+=i
                elif currsum+i==fixsum: 
                    nosa+=1
                    minsumsubarray=max(minsumsubarray,currsum+i)
                    currsum=0
                else :
                    nosa+=1
                    minsumsubarray=max(minsumsubarray,currsum)
                    currsum=i
           # print('srk',nosa,minsumsubarray,split)
            if currsum > 0:
                nosa += 1
                minsumsubarray = max(minsumsubarray, currsum)
            return nosa,minsumsubarray
        ans=0
        while l<=r:
            m=l+((r-l)//2)
            if numberofsubarrayforfixsum(m)[0]<=k:
                ans=numberofsubarrayforfixsum(m)[1]
                r=m-1
            else :
                l=m+1
        return ans
                
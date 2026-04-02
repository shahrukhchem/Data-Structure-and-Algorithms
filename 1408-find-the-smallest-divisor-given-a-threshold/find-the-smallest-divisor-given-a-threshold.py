class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumofdivisor(nums,divisor):
            divisorsum=0
            for i in nums:
                divisorsum+= (i + divisor - 1) // divisor
            return divisorsum
        n=len(nums)
        k=max(nums)
        l=1
        r=k
        while l<=r:
            m=l+((r-l)//2)
            if sumofdivisor(nums,m)<=threshold:
                ans=m
                r=m-1
            else:
                l=m+1
        return ans
        ''''
        for i in range(1,k+1):
            print(sumofdivisor(nums,i))
            if sumofdivisor(nums,i)<=threshold:
                return i
        '''
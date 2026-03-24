class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #unrotate
        n=len(nums)
        i=0
        found=False
        if n>1:
            for i in range(1,n):
                if nums[i]<nums[i-1]:
                    found = True
                    break
        if not found:
            i = 0
        unrotatenums=nums[i:]+nums[:i]
        #binarysearch 
        L=0
        R=n-1
        while L<=R:
            M=L+((R-L)//2)
            
            if unrotatenums[M]==target:
                return (M + i) % n
            elif target<unrotatenums[M]:
                R=M-1
            else:
                L=M+1
        return -1
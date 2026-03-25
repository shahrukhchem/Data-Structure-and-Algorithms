class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(arr,target):
            n=len(arr)
            l=0
            r=n-1
            while l<=r:
                M=l+((r-l)//2)
                if arr[M]==target:
                    return True
                elif arr[M]<target:
                    l=M+1
                else:
                    r=M-1
            return False
                
        for i in matrix:
            if i[0]<=target and i[-1]>=target:
               return  binarysearch(i,target)
        return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(arr,target,n):
            l=0
            r=n-1
            while l<=r:
                m=l+((r-l)//2)
                if arr[m]==target:
                    return True
                elif arr[m]<target:
                    l=m+1
                else:
                    r=m-1
            return False
        nor=len(matrix)
        noc=len(matrix[0])
        for i in range(0,nor):
            if matrix[i][0]<=target and binarysearch(matrix[i],target,noc):
                        return True
        return False

        
        
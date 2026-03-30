class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarysearch(arr,binarysearchtarget,newl):
            n=len(arr)
            l= newl
            r=n-1
            while l<=r:
                m=l+((r-l)//2)
                if arr[m]==binarysearchtarget:
                    return m
                elif arr[m]>binarysearchtarget:
                    r=m-1
                else:
                    l=m+1
            return -1
        n=len(numbers)
        for i in range(0,n):
            binarysearchtarget=target-numbers[i]
            res=binarysearch(numbers,binarysearchtarget,i+1)
            if res==-1:
                continue
            return [i+1,res+1]

        
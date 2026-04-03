class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+ nums2
        arr=sorted(arr)
        
        if len(arr)%2==0:
            med=arr[len(arr)//2]+arr[(len(arr)//2)-1]
            return med/2

        else:
            return(arr[len(arr)//2])
        
        return len(arr)
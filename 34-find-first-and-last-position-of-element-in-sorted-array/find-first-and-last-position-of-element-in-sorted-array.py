class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(arr,target,pos):
            n=len(arr)
            l=0
            r=n-1
            ans=-1
            while l<=r:
                m=l+((r-l)//2)
                if arr[m]==target:
                    ans=m
                    if pos=='f':
                        r=m-1
                    else:
                        l=m+1
                elif arr[m]>target:
                    r=m-1
                else:
                    l=m+1
            return ans
        return [binarysearch(nums,target,'f'),binarysearch(nums,target,'l')]




        
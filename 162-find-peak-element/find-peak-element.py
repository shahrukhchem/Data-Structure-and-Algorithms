class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        k=max(nums)
        n=len(nums)
        for i in range(0,n):
            if nums[i]==k:
                 return i
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        k=n*(n+1)/2
        sums=0
        for i in nums:
            sums+=i
        return int(k-sums)
        
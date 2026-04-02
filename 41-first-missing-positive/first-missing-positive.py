class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=min(nums)
        l=max(nums)
        counter={}
        for j in nums:
            counter[j]=1
        for i in range(1,l+1):
            if i not in counter:
                return i
        if l>0:
            return l+1
        else:
            return 1
            
        
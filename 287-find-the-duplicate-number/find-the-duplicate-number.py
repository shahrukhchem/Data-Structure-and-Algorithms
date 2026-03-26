class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       n=len(nums)
       countdic={}
       for i in nums:
        if i in countdic:
            countdic[i]+=1
            if countdic[i]==2:
                return i
        else:
             countdic[i]=1
        
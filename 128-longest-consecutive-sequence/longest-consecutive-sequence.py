class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        highseq=0
        for i in nums:
            maxcount=1
            flag=100
            if i-1 in nums:
                continue
            while flag !=-1:
                if i+1 in nums:
                    maxcount+=1
                    i=i+1
                else:
                    flag=-1
            if highseq<=maxcount:
                highseq=maxcount
        return highseq

        
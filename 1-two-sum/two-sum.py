class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        n=len(nums)
        c={}
        for i in range(0,n):
            if nums[i] in c:
                c[nums[i]].append(i)
            else:
                c[nums[i]]=[i]
        r=n-1
        for i in range(0,n):
            fa=i
            currtarget=target-nums[i]
            if currtarget==nums[i]:
                if len(c[currtarget])==1:
                    continue
            if currtarget in c:
                if currtarget==nums[i]:
                    return [fa,c[nums[i]][1]]
                else:
                    return [fa,c[currtarget][0]]
        
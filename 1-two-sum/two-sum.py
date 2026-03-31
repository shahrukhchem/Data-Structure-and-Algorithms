class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortednums=sorted(nums)
        l=0
        n=len(nums)
        c={}
        for i in range(0,n):
            if nums[i] in c:
                c[nums[i]].append(i)
            else:
                c[nums[i]]=[i]
        r=n-1
        while l<r:
            if sortednums[l]+sortednums[r]==target:
                if sortednums[l]==sortednums[r]:
                    return [c[sortednums[l]][0],c[sortednums[r]][1]]
                else:
                    return [c[sortednums[l]][0],c[sortednums[r]][0]]
                    
            elif sortednums[l]+sortednums[r]>target:
                r=r-1
            else:
                l=l+1
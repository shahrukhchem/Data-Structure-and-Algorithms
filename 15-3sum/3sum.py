class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortnum=sorted(nums)
        n=len(nums)
        res=[]
        seen = set()
        for i in range(0,n-2):
            target=-1*sortnum[i]
            l=i+1
            r=n-1
            while l<r:
                triplet = (sortnum[l],sortnum[r],sortnum[i])
                key = triplet
                if key in seen:
                    l=l+1
                    continue   
                else:
                    if sortnum[l]+sortnum[r]+sortnum[i]==0:
                        seen.add(key)
                    elif sortnum[l]+sortnum[r]>target:
                        r=r-1
                    elif sortnum[l]+sortnum[r]<target:
                        l=l+1
                
        return list(seen)
    
        
 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates={} 
        ind=0
        for i in nums:
            if i in duplicates:
                 lst = duplicates[i][1]  
                 lst.append(ind) 
                 count=duplicates[i][0]+1
                 duplicates[i]=(count, lst)
                 if count>=2:
                    if lst[-1] - lst[-2] <= k:
                        return True


            else:
                duplicates[i]=(1,[ind])
            ind+=1
        return False
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol=[]
        res=[]
        def backtrack(i):
            if len(sol)==n:
                res.append(sol[:])
                return 
            for j in range(0,n):
                if nums[j] not in sol:
                    sol.append(nums[j])
                    backtrack(j)
                    sol.pop()
        backtrack(0)
        return res


            
        
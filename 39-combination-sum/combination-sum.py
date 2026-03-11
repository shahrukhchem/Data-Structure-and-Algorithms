class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol,res=[],[]
        n=len(candidates)
        def backtrack(i):
            if sum(sol)==target:
                res.append(sol[:])
                return 
            if sum(sol)>target or i==n:
                return 
            backtrack(i+1)
            sol.append(candidates[i]) 
            backtrack(i)
            sol.pop()
        backtrack(0)
        return res


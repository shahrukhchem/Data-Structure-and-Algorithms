class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol,res=[],[]
        n=len(candidates)
        def dfsrecur(start,curr_sum,numbers):
            if curr_sum==target:
                res.append(numbers.copy())
                return
            if curr_sum>target:
                return
            for num in range(start,len(candidates)):
                numbers.append(candidates[num])
                dfsrecur(num,curr_sum + candidates[num],numbers)
                numbers.pop()
        dfsrecur(0,0,[])
        return res


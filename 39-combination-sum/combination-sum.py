class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol,res=[],[]
        n=len(candidates)
        def dfsrecur(start,numbers):
            if sum(numbers)==target:
                res.append(numbers.copy())
                return
            if sum(numbers)>target:
                start=start+1
                return
            for num in range(start,len(candidates)):
                numbers.append(candidates[num])
                dfsrecur(num,numbers)
                numbers.pop()
        dfsrecur(0,[])
        return res


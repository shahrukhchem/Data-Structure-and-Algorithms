class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        found = set()
        stack=[([],candidates)]
        totalsol=0
        res=[]
        while stack:
            currentchoice,optionsavailable=stack.pop()
            if not optionsavailable:
                if sum(currentchoice)==target and tuple(currentchoice) not in found:
                                            totalsol+=1
                                            found.add(tuple(currentchoice))
                                            res.append(currentchoice)
                continue
            if sum(currentchoice)==target and tuple(currentchoice) not in found:
                                totalsol+=1
                                found.add(tuple(currentchoice))
                                res.append(currentchoice)
                                
            if sum(currentchoice) < target:
                stack.append((currentchoice+[optionsavailable[-1]],optionsavailable))
            stack.append((currentchoice,optionsavailable[:-1]))
        return res
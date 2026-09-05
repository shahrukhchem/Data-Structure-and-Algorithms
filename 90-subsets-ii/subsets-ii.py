class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        found = set()
        stack=[([],nums)]
        totalsol=0
        res=[]
        while stack:
            currentchoice,optionsavailable=stack.pop()
            k=tuple(sorted(currentchoice))
            if not optionsavailable:
                if  k not in found:
                    found.add(k)
                    res.append(currentchoice)
                continue
            if  k not in found:
                    found.add(k)
                    res.append(currentchoice)
            stack.append((currentchoice+[optionsavailable[-1]],optionsavailable[:-1]))
            stack.append((currentchoice,optionsavailable[:-1]))
        return res
        
        
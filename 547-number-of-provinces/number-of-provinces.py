from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        graph=defaultdict(list)
        for ro in range(0,n):
            for col in range(0,len(isConnected[ro])):
                if isConnected[ro][col]==1:
                  graph[ro+1].append(col+1)
        
        def dfsrecur(node):
            for neinode in graph[node]:
                if neinode not in seen:
                    seen.add(neinode)
                    dfsrecur(neinode)
        seen=set()
        res=[]
        for n  in range(1,n+1):
            if n not in seen:
                dfsrecur(n)
                res.append(tuple(seen))
        res=set(res)
        return len(res)


        
        
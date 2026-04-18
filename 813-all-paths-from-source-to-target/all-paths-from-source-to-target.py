from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        def buildgraph(edgelist):
            graph=defaultdict(list)
            for node in range(0,n):
                for j in edgelist[node]:
                    graph[node].append(j)
            return graph
        def dfsongraph(graph,source,destination,paths):
            visited = set()
            stack = [(source,[source])]
            while stack:
                node,path = stack.pop()
                if node==destination:
                    paths.append(path)
                for neighbor in graph[node]:
                    stack.append((neighbor,path+[neighbor]))   
            return paths
        gr=buildgraph(graph)
        return dfsongraph(gr,0,n-1,[])
        
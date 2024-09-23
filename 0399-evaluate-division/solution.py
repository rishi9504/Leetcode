from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (A,B), value in zip(equations,values):
            graph[A][B] = value
            graph[B][A] = 1/value
        def dfs(s,e,v):
            if s not in graph or e not in graph:
                return -1.0
            if s==e:
                return 1.0
            v.add(s)
            for i,val in graph[s].items():
                if i not in v:
                    res = dfs(i,e,v)
                    if res!=-1.0:
                        return res*val
            return -1.0
        res=[]
        for C,D in queries:
            if C in graph and D in graph:
                res.append(dfs(C,D,set()))
            else:
                res.append(-1.0)
        return res                                    

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        #building adj list for graph
        graph = [[] for _ in range(n)]
        for i in range(n):
            x,y,r = bombs[i]
            for j in range(n):
                if i!=j:
                    x1,y1,_ = bombs[j]
                    # check if bombs are in range
                    if (x-x1)**2+(y-y1)**2 <= r**2:
                        graph[i].append(j)

        # adj list is done
        # do dfs
        def dfs(node, v):
            v.add(node)
            c=1
            for n in graph[node]:
                if n not in v:
                    c+=dfs(n,v)
            return c



        md=0
        for i in range(n):
            v=set()
            md = max(md,dfs(i,v))
        return md            


        

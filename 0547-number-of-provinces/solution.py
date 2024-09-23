class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        v=set()
        def dfs(c):
            v.add(c)
            for i in range(n):
                if isConnected[c][i]==1 and i not in v:
                    dfs(i)
        count = 0
        for city in range(n):
            if city not in v:
                dfs(city)
                count+=1
        return count                    
        

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]]=(i,j)
        rpc=[0]*m
        cpc = [0]*n 
        for i,num in enumerate(arr):
            r,c = pos[num]
            rpc[r]+=1
            cpc[c]+=1
            if rpc[r]==n or cpc[c]==m:
                return i
        return -1              
        

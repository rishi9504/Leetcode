class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        m,n = len(land),len(land[0])
        def dfs(row,col):
            #dfs will stop if value is not 1 or values not on board
            if row>=m or col>=n or land[row][col]==0:
                return (0,0)
            land[row][col] = 0
            # recursively search for the right and below square
            r1,c1 = dfs(row+1,col)
            r2,c2 = dfs(row,col+1)
            hr = max(r1,r2,row)
            hc = max(c1,c2,col)
            return (hr,hc)
        # iterate thru all positions in square,left-right & top-bottom    
        for i in range(m):
            for j in range(n):
                #if land[i][j]==1, start dfs from that co ordinate
                if land[i][j]==1:
                    x,y = dfs(i,j)
                    ans.append([i,j,x,y])
        return ans                    
        

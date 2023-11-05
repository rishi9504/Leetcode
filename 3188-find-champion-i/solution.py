class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        team_strengths = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    if grid[i][j] == 1:
                        team_strengths[i] += 1
                    else:
                        team_strengths[j] += 1

        champion = 0
        max_strength = team_strengths[0]

        for i in range(1, n):
            if team_strengths[i] > max_strength:
                champion = i
                max_strength = team_strengths[i]

        return champion
        

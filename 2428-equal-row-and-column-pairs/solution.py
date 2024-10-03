class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = Counter(zip(*grid))
        grid = Counter(map(tuple,grid))
        return sum(transpose[t]*grid[t] for t in transpose)
        

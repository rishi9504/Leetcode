class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        vals = []
        for x, y in logs: 
            vals.append((x, 1))
            vals.append((y, -1))
        ans = prefix = most = 0
        for x, k in sorted(vals): 
            prefix += k
            if prefix > most: 
                ans = x
                most = prefix 
        return ans 

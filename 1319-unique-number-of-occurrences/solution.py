class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n={} #create dict for storing frequency
        for i in arr:
            n[i] = n.get(i,0)+1
        return len(n) == len(set(n.values()))    

        

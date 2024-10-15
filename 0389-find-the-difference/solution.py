class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = {}
        for a in s:
            if a in counts:
                counts[a]+=1
            else:
                counts[a]=1
        for a in t:
            if a not in counts:
                return a 
            else:
                counts[a]-=1
        for k,v in counts.items():
            if v!=0:
                return k

        return list(set(t)-set(s))[0]
        

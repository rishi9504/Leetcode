class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = {score[i]: i for i in range(len(score))}
        score.sort(reverse=True)
        res = ["" for i in range(len(score))]
        for i in range(len(score)):
            if i ==0:
                res[s[score[i]]] = "Gold Medal"
            elif i ==1:
                res[s[score[i]]] = "Silver Medal" 
            elif i ==2:
                res[s[score[i]]] = "Bronze Medal"
            else:
                res[s[score[i]]] = str(i+1)
        return res                   
        

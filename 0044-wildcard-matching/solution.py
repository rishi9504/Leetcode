class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i,j = 0,0
        star = -1
        while i < len(s):
            if j >= len(p) or (p[j] not in {'*','?'} and p[j]!=s[i]):
                if star == -1:
                    return False
                j = star+1
                star_i+=1
                i = star_i
            elif p[j] == '*':
                star = j
                star_i = i
                j+=1
            else:
                i +=1
                j +=1
        while j < len(p):
            if p[j] != '*':
                return False
            j += 1
        return True    
        

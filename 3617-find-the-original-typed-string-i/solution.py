class Solution:
    def possibleStringCount(self, word: str) -> int:
        po = []
        po.append(word)
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                pw = word[:i]+word[i+1:]
                po.append(pw)
        return len(po)    
        

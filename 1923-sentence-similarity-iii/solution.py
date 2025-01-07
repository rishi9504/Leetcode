class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split()
        w2 = sentence2.split()

        if len(w1)>len(w2):
            w1,w2 = w2,w1
        l,j = 0,0
        while l<len(w1) and w1[l]==w2[l]:
            l+=1
        while j<len(w1) and w1[-(j+1)] == w2[-(j+1)]:
            j+=1
        return l+j>=len(w1)
        

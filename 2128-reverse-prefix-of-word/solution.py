class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #easy method 
        # i = word.find(ch)
        # if i==-1:
        #     return word
        # return word[:i+1][::-1]+word[i+1:] 

        # two pointer approach
        i = word.find(ch)
        if i==-1:
            return word

        wl = list(word)
        l,r = 0,i
        while l<r:
            wl[l],wl[r] = wl[r],wl[l]
            l+=1
            r-=1
        return ''.join(wl)        


        

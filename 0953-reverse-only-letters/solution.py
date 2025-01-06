class Solution:
    def reverseOnlyLetters(self, S):
        # S[::-1]
        # r = [s for s in S if s.isalpha()]
        # return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))

        #update, use two pointer approach, swap if isalpha or else move the l or r pointer
        s = list(S)
        l,r = 0,len(S)-1
        while l<r:
            if not s[l].isalpha():
                l+=1
                continue
            if not s[r].isalpha():
                r-=1
                continue
            else:
                s[l],s[r] = s[r],s[l] 
                l+=1
                r-=1
        return ''.join(s)               


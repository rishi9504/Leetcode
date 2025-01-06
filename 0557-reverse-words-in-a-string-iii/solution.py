class Solution:
    def reverseWords(self, s: str) -> str:
        sl = list(s)
        n = len(s)
        def reverseWord(st,en):
            while st<en:
                sl[st],sl[en] = sl[en],sl[st]
                st+=1
                en-=1
        i=0
        while i<n:
            while i<n and sl[i]==' ':
                i+=1
            st=i
            while i<n and sl[i]!= ' ':
                i+=1
            en = i-1
            if st<n:
                reverseWord(st,en)
        return ''.join(sl)            

        

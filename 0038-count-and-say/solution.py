class Solution:
    def countAndSay(self, n: int) -> str:
        return ''.join([str(c) for c in self.count(0,n-1,[1])])[::-1]
    
    def count(self,cn,n,seq):
        if n==cn:
            return seq
        new_seq = self.compress(seq)
        return self.count(cn+1,n,new_seq)

    def compress(self,seq):
        res=[]
        cnt=[seq[0],0]
        for i in seq:
            if i==cnt[0]:
                cnt[1]+=1
            else:
                res.extend(cnt)
                cnt=[i,1]
        res.extend(cnt)
        return res





        

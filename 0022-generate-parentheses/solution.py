class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out=set()
        res= self.generate(n,0,0,'',out)
        return out



    def generate(self,n, l,r, s,res):
        if len(s)==n*2:
            res.add(s)
            # print('res is ',res)
            return
        # print(l,r,s,res)
        if l<n:
            self.generate(n,l+1,r,s+'(',res)
        if r<l:
            self.generate(n,l,r+1,s+')',res)
       

#         The idea is to add ')' only after valid '('
# We use two integer variables left & right to see how many '(' & ')' are in the current string
# If left < n then we can add '(' to the current string
# If right < left then we can add ')' to the current string
       

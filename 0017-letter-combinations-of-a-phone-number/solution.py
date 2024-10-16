class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dl={
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz',
        }
        def bt(num,com):
            if num==len(digits):
                res.append(com[:])
                return
            for l in dl[int(digits[num])]:
                bt(num+1,com+l)
        res=[]
        bt(0,"")
        return res          
        

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for idx in range(len(num)-1,-1,-1):
            i=num[idx]
            # print(i)
            if i=='0':
                continue
            if int(i)%2!=0:
                return (num[0:idx+1])

        return ""
        

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr,n = [],len(s)
        for i in range(n):
            if s[i]==c:
                arr.append(i)
        ans=[]
        ind = 0
        for i in range(n):
            if s[i]==c:
                ans.append(0)
                ind+=1
            elif i < arr[0]:
                ans.append(arr[0]-i)
            elif i>arr[-1]:
                ans.append(i-arr[-1])
            else:
                ans.append(min((arr[ind]-i),(i-arr[ind-1])))
        return ans                            
        

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mind =arr[1]-arr[0]
        for i in range(len(arr)-1):
            d=arr[i+1]-arr[i]
            if d< mind:
                mind=d
        res=[]
        for i in range(len(arr)-1):
            if arr[i+1]==arr[i]+mind:
                res.append([arr[i],arr[i+1]])
        return res


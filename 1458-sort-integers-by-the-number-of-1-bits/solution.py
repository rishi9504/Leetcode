class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sorter(x):
            # print(x,bin(x))
            return (bin(x)).count('1'),x
        return sorted(arr,key=sorter,reverse=False)
        

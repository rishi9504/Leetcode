class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # two pointer approach

        for row in image:
            l,r = 0,len(row)-1
            while l<=r:
                row[l],row[r] = 1-row[r],1-row[l]
                l+=1
                r-=1
        return image        

        

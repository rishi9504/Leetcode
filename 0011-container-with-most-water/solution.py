class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        #started with widest seperation of the lines
        max_area = (right-left) * min(height[right],height[left])

        while left < right : #any lesser sep should have more area than prev calc.
            if height[left] < height[right]: 
                left+=1
            else:
                right-=1
            #calculate max area and newly calculated area    
            max_area = max(max_area,(right-left)*min(height[right],height[left]))
        return max_area            
        

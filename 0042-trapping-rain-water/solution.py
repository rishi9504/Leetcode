class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        highest_right = [0]*len(height)
        for i in range(len(height)-2,-1,-1):
            highest_right[i] = max(highest_right[i+1], height[i+1])
        highest_left,depth = [0]*len(height) , 0
        for i in range(1,len(height)):
            highest_left[i] = max(highest_left[i-1], height[i-1])
            depth+= max(0,min(highest_left[i],highest_right[i])-height[i])
        return depth    

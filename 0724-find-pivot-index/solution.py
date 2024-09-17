class Solution(object):
    def pivotIndex(self, nums):
        # maintain two array for sum of left and right
        #check if they are equal at any point
        leftSum, rightSum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx      
            leftSum += ele
        return -1       

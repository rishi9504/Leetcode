class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))] #default to 1 per child
        right = [1 for _ in range(len(ratings))]

        for i in range(1,len(ratings)):  #increase above previous child if greater rating
            if ratings[i]> ratings[i-1]:
                left[i] = left[i-1]+1
        candies = left[-1]   #rightmost child not included in the loop
        for i in range(len(ratings)-2,-1,-1): #increase in greater rating
            if ratings[i]> ratings[i+1]:
                right[i] = right[i+1]+1
            candies += max(left[i],right[i]) #child gets more due to left and right
        return candies        







        

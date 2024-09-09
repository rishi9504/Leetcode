# 605. Can Place Flowers
# Solved
# Easy
# Topics
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


# greedy approach
# This function checks if it's possible to plant `n` new flowers in a flowerbed without planting them in adjacent plots. It iterates through the flowerbed, and for each empty plot, it checks if the adjacent plots are also empty. If they are, it plants a flower in the current plot and increments the count. The function returns `True` if it can plant at least `n` flowers, and `False` otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i]==0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == l - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i]=1
                    count +=1
                    if count >= n:
                        return True
        return count >= n  
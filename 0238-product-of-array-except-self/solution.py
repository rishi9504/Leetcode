class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#          "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer" means that for a given array nums containing integers, the product of any consecutive subarray (prefix or suffix) within nums will not exceed the range of a 32-bit integer.

# In other words, if you were to calculate the product of any sequence of numbers from the beginning (prefix) or the end (suffix) of the array nums, the result will always be within the valid range of a 32-bit signed integer
        products = [1]
        for i in range(1,len(nums)):
            products.append(nums[i-1]*products[-1])
        right_p = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *=right_p
            right_p *= nums[i]
        return products        
        

from math import gcd
from functools import reduce
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # def lcm(a,b):
        #     return abs(a*b)//gcd(a,b)

        # def lcm_list(nums):
        #     return reduce(lcm,nums,1)

        # def factor_score(nums):
        #     return gcd(nums[0],nums[0]*lcm_list(nums))

        
        # n=len(nums)
        # if n==1:
        #     return factor_score(nums)


        # prefixGCD= [0]*n
        # suffixGCD = [0]*n
        # prefixGCD[0] = nums[0]
        # for i in range(1,n):
        #     prefixGCD[i] = gcd(prefixGCD[i-1],nums[i])
        # suffixGCD[n-1] = nums[n-1]
        # for i in range(n-2,-1,-1):
        #     suffixGCD[i] = gcd(suffixGCD[i+1],nums[i])
        # max_score=0
        # for i in range(n):
        #     if i==0:
        #         new_gcd = suffixGCD[1]
        #     elif i==n-1:
        #         new_gcd = prefixGCD[n-2]
        #     else:
        #         new_gcd = gcd(prefixGCD[i-1],suffixGCD[i+1])
        #     remaining_nums = nums[:i]+nums[i+1:]
        #     new_lcm=lcm_list(remaining_nums)
        #     new_score = new_gcd*new_lcm
        #     max_score = max(max_score,new_score)
        # total_gcd = prefixGCD[-1]
        # total_lcm = lcm_list(nums)
        # max_score = max(max_score,total_gcd*total_lcm)
        # return max_score

        def lcm(a, b):
            return abs(a * b) // gcd(a, b)
    
        def lcm_list(nums):
            return reduce(lcm, nums, 1)  
        
        def factor_score(nums):
            return gcd(nums[0], nums[0]) * lcm_list(nums)
        
        def maxFactorScore(nums):
            n = len(nums)
            
            if n == 1:
                return factor_score(nums)  # Only one number, no removal possible
            
            prefixGCD = [0] * n
            suffixGCD = [0] * n
            
            prefixGCD[0] = nums[0]
            for i in range(1, n):
                prefixGCD[i] = gcd(prefixGCD[i - 1], nums[i])
            
            suffixGCD[n - 1] = nums[n - 1]
            for i in range(n - 2, -1, -1):
                suffixGCD[i] = gcd(suffixGCD[i + 1], nums[i])
            
            max_score = 0
            
            for i in range(n):
                if i == 0:
                    new_gcd = suffixGCD[1]  
                elif i == n - 1:
                    new_gcd = prefixGCD[n - 2]  
                else:
                    new_gcd = gcd(prefixGCD[i - 1], suffixGCD[i + 1])
                
                remaining_nums = nums[:i] + nums[i + 1:]
                new_lcm = lcm_list(remaining_nums)
                
                new_score = new_gcd * new_lcm
                max_score = max(max_score, new_score)
            
            total_gcd = prefixGCD[-1]  
            total_lcm = lcm_list(nums)  
            max_score = max(max_score, total_gcd * total_lcm)
            
            return max_score
        return maxFactorScore(nums)    
                

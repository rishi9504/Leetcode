class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        # while numbers[r]>target:
        #     r-=1
        while l<=r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            # if target < numbers[r]:
            if numbers[l]+numbers[r]<target:
                # r-=1
                l+=1
            else:
                r-=1
                # l+=1


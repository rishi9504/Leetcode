class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # Now first < num, if num <= second then try to make `second` as small as possible
                second = num
            else:  # Now first < second < num
                return True
        return False

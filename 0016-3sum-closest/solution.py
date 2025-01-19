

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Finds a triplet in the given list of numbers that has a sum closest to the given target.
        """
        # First, sort the list of numbers. This is because we want to use a two-pointer technique
        # to find the triplet, and the two-pointer technique relies on the list being sorted.
        nums.sort()

        # Initialize a variable to store the difference between the target and the sum of the triplet.
        # We initialize it to infinity because we want to find the smallest difference possible.
        diff = float('inf')

        # Iterate over the list of numbers. We don't need to check the last two elements because
        # the two-pointer technique will cover them.
        for i in range(len(nums)-2):
            # Initialize two pointers, one at the next element after i, and one at the end of the list.
            start = i + 1
            end = len(nums) - 1

            # Iterate until the two pointers meet.
            while start < end:
                # Calculate the sum of the three numbers at i, start, and end.
                sum = nums[i] + nums[start] + nums[end]

                # If the sum is equal to the target, return it.
                if sum == target:
                    return target

                # If the sum is closer to the target than the current difference, update the difference
                # and the answer.
                if abs(target - sum) < diff:
                    diff = abs(target - sum)
                    ans = sum

                # If the sum is greater than the target, move the end pointer to the left.
                # If the sum is less than the target, move the start pointer to the right.
                if sum > target:
                    end -= 1
                else:
                    start += 1

        # Return the answer.
        return ans
            
        

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine the two input sorted arrays into a single list
        combined = nums1 + nums2
        
        # Sort the combined list; sorting is O(n log n)
        combined.sort()
        
        # Calculate the total number of elements in the combined list
        total_length = len(combined)
        
        # Check if the number of elements is odd
        if total_length % 2 != 0:
            # If odd, the median is the middle element
            median = combined[total_length // 2]
        else:
            # If even, the median is the average of the two middle elements
            mid1 = total_length // 2
            mid2 = mid1 - 1
            median = (combined[mid1] + combined[mid2]) / 2
        
        # Return the calculated median value
        return median






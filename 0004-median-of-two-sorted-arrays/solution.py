class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # Combine the two input sorted arrays into a single list
        # combined = nums1 + nums2
        
        # # Sort the combined list; sorting is O(n log n)
        # combined.sort()
        
        # # Calculate the total number of elements in the combined list
        # total_length = len(combined)
        
        # # Check if the number of elements is odd
        # if total_length % 2 != 0:
        #     # If odd, the median is the middle element
        #     median = combined[total_length // 2]
        # else:
        #     # If even, the median is the average of the two middle elements
        #     mid1 = total_length // 2
        #     mid2 = mid1 - 1
        #     median = (combined[mid1] + combined[mid2]) / 2
        
        # # Return the calculated median value
        # return median
    
        # Solving using binary search, time complexity is O(log(min(n1,n2)))
        
        n1 = len(nums1)
        n2 = len(nums2)
        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        # Binary search
        # Calculate the total number of elements in the two arrays
        n = n1 + n2
        
        # Calculate the left partition point for the binary search
        # The left partition point is the index of the element in the combined array that would be the median
        # If the total number of elements is odd, the median is the element at the left partition point
        # If the total number of elements is even, the median is the average of the two elements at the left and right partition points
        l = (n1 + n2 + 1) // 2
        
        # Initialize the binary search range
        low = 0
        high = n1
        
        # Perform the binary search
        while low <= high:
            # Calculate the mid points in both arrays
            mid1 = (low + high) // 2
            mid2 = l - mid1
            
            # Get the left and right elements at the current mid points
            # The left element is the element to the left of the mid point
            # The right element is the element to the right of the mid point
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            # Get the left and right elements at the current mid points
            if mid1<n1:
                l1 = nums1[mid1]
            if mid2<n2:
                l2 = nums2[mid2]
            if mid1-1>=0:
                r1 = nums1[mid1-1]
            if mid2-1>=0:
                r2 = nums2[mid2-1]
            
            # If l1 <= r2 and l2 <= r1, the current partition is correct
            if l1<=r2 and l2<=r1:
                if n%2==1:
                    # If the total number of elements is odd, the median is the max of l1 and l2
                    return max(l1,l2)
                else:
                    # If the total number of elements is even, the median is the average of the two middle elements
                    return (max(l1,l2)+min(r1,r2))/2.0
            elif l1>r2:
                # If l1 > r2, the partition is incorrect, so move the right pointer to the left
                high = mid1-1
            else:
                # If l1 <= r2, the partition is incorrect, so move the left pointer to the right
                low = mid1+1
        # If the loop completes and the partition is still incorrect, return 0
        return 0






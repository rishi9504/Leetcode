class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(subarray, k):
            left, right = 0, k - 1
            while left < right:
                subarray[left], subarray[right] = subarray[right], subarray[left]
                left += 1
                right -= 1

        result = []
        n = len(arr)

        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))

            if max_index != size - 1:
                if max_index != 0:
                    result.append(max_index + 1)
                    flip(arr, max_index + 1)

                result.append(size)
                flip(arr, size)

        return result
        

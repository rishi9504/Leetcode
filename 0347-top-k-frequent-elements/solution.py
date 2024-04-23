class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in hashMap.items():
            bucket[value].append(key)
        
        result = []
        for i in range(len(bucket) -1 , 0 , -1):
            values = bucket[i]
            for val in values:
                result.append(val)
                if len(result) == k:
                    return result
        return [None]

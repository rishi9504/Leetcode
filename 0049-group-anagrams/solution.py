class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         # Create a dictionary to store the groups of anagrams
        anagram_groups = {}
    
    # Iterate through each string in the array
        for s in strs:
        # Sort the string to use it as a key in the dictionary
            sorted_s = ''.join(sorted(s))
        
        # If the sorted string is not in the dictionary, add it with an empty list as the value
            if sorted_s not in anagram_groups:
                anagram_groups[sorted_s] = []
        
        # Add the original string to the list of anagrams
            anagram_groups[sorted_s].append(s)
    
    # Return the values from the dictionary as the grouped anagrams
        return list(anagram_groups.values())

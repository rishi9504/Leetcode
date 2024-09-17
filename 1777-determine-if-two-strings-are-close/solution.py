# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if set(word1) == set(word2) and len(word1)==len(word2):
#             return True
#         return False    


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        

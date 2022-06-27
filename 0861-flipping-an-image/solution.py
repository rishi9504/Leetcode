class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        inverse_values = [[0 if i else 1 for i in values] for values in image]
        flip_value = [x[::-1] for x in inverse_values]
        return flip_value
        

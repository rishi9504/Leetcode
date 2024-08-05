# # class Solution:
# #     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
# #         # l1,l2=len(text1),len(text2)
# #         # longest = text1 if l1 > l2
# #         long,short = sorted([text1,text2],key=len)
# #         ll=len(long)
# #         sl = len(short)
# #         sol_idx = []
# #         for i,c in enumerate(short):
# #             for j,c1 in enumerate(long):
# #                 if c1==c:
# #                     sol_idx.append((i,j,))
        
# #         for i,j in sol_idx:
# #             i2,j2=i,j
# #             while i2 < sl and j2 < ll:

# lookup = None
# def gen_lookup(m,n):
#     global lookup
#     lookup =  [[None]*n]*m

# class Solution:
#     def lcs(self,X,Y,m,n):
#         global lookup
#         if m==0 or n==0:
#             return 0
#         # if lookup[m-1][n-1] is not None:
#         #     return lookup[m-1][n-1]
#         elif X[m-1] == Y[n-1]:
#             ret = 1 + self.lcs(X,Y,m-1,n-1)
#             lookup[m-1][n-1] = ret
#             return ret
#         else:
#             ret =max(self.lcs(X,Y,m,n-1),self.lcs(X,Y,m-1,n))  
#             return ret


#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m= len(text1)
#         n=len(text2)
#         gen_lookup(m,n)
#         return self.lcs(text1,text2,m,n)



        

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of both input strings
        len_text1, len_text2 = len(text1), len(text2)
      
        # Initialize a 2D array (list of lists) with zeros for dynamic programming
        # The array has (len_text1 + 1) rows and (len_text2 + 1) columns
        dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]
      
        # Loop through each character index of text1 and text2
        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                # If the characters match, take the diagonal value and add 1
                if text1[i - 1] == text2[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    # If the characters do not match, take the maximum of the value from the left and above
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
      
        # The bottom-right value in the matrix contains the length of the longest common subsequence
        return dp_matrix[len_text1][len_text2]        

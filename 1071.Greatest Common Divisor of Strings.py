# 1071. Greatest Common Divisor of Strings
# Solved
# Easy
# Topics
# Companies
# Hint
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.




# This function calculates the greatest common divisor (GCD) of two input strings `str1` and `str2`. However, instead of finding the GCD of their lengths, it finds the largest string that can be concatenated to form both `str1` and `str2`. If no such string exists, it returns an empty string.

# The function first checks if concatenating `str1` and `str2` in either order produces the same result. If not, it returns an empty string. Otherwise, it calculates the GCD of the lengths of `str1` and `str2` and returns the substring of `str1` up to that length.

# In essence, this function finds the largest string that can be repeated to form both input strings.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1),len(str2))]  
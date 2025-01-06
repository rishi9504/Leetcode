class Solution:
    def validPalindrome(self, s: str) -> bool:
        # should be a medium, tagged easy...venting
        # use two pointer approach with two functions
        # check palindrome in one and check mismatch may be in other
        # if s[l]=s[r], l++,r--
        # if s[l] != s[r] ,check if string from index l to r-1(neglecting s[r]) or 
        # string from index l+1 to r(neglecting s[l]) is palindrom.
        # If both of them are not palindrom, return false. Otherwise, return true.

        def isPalindrome(subs,l,r):
            while l<r:
                if subs[l]!=subs[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r = 0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return isPalindrome(s,l+1,r) or isPalindrome(s,l,r-1)
            l+=1
            r-=1
        return True                


        

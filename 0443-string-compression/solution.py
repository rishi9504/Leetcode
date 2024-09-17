class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        string = ""
        for i in range(len(chars)):
            count+=1
            if i+1>=len(chars) or chars[i] != chars[i+1]:
                string+=chars[i]
                if count>1:
                    string+=str(count)
                count=0
        chars[:] = list(string)    
        return len(string)        
        

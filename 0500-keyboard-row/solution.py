class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = set("qwertyuiop")
        s = set("asdfghjkl")
        t = set("zxcvbnm")
        ans = []
        for word in words:
            if len(set(word.lower()) | f) == len(f) or len(set(word.lower()) | s) == len(s) or len(set(word.lower()) | t) == len(t):
                ans.append(word)

        return ans
        

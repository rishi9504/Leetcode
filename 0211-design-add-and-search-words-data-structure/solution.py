class WordDictionary:

    def __init__(self):
        self.dict = set()
        self.len_dict = {}
        self.search_cache = {}

    def addWord(self, word: str) -> None:
        if word not in self.dict:
            self.search_cache = {}
            self.dict.add(word)
            n = len(word)
            if n not in self.len_dict:
                self.len_dict[n] = {word}
            else: self.len_dict[n].add(word)


    def search(self, word: str) -> bool:
        if word in self.search_cache:
            return self.search_cache[word]
        if word in self.dict:
            return True
        n = len(word)
        if n not in self.len_dict:
            return False
        found = False
        for dict_word in self.len_dict[n]:
            is_this_word = True
            for c, d_c in zip(word, dict_word):
                if c != '.' and c != d_c:
                    is_this_word = False 
                    break
            if is_this_word:
                found = True
                break
        self.search_cache[word] = found
        return found

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

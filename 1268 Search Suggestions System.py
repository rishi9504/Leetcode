# 1268. Search Suggestions System
# Solved
# Medium

# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord 
# is typed. Suggested products should have common prefix with searchWord. If there are more than three products
# with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.


        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Insert a product into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Maintain a list of lexicographically smallest suggestions
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
    
    # Search the Trie for a given prefix and collect up to 3 suggestions
    def search(self, prefix):
        node = self.root
        result = []
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                # If the prefix is not found, return empty lists for the rest of the characters
                while len(result) < len(prefix):
                    result.append([])
                break
        return result

class Solution:
    def suggestedProducts(self, products, searchWord):
        # Step 1: Sort the products lexicographically
        products.sort()
        
        # Step 2: Build the Trie
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        # Step 3: For each prefix of searchWord, retrieve the suggestions
        return trie.search(searchWord)

